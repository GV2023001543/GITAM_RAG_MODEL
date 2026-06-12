from __future__ import annotations

import os
import io
import sqlite3
import tempfile
from langgraph.graph import StateGraph, START, END
from typing import Annotated, Any, Dict, Optional, TypedDict, List

import yfinance as yf

from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

# ---------------------------------------------------------------------------
# college_rag — imported here so it shares the same embeddings instance
# ---------------------------------------------------------------------------
from college_rag import build_college_index, college_rag_search, college_index_ready, get_college_index_meta  # noqa: E402

# ---------------------------------------------------------------------------
# 0. Per-user API key store  (SQLite, survives Streamlit re-runs)
# ---------------------------------------------------------------------------

_KEY_DB_PATH = "user_api_keys.db"

def _get_key_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(_KEY_DB_PATH, check_same_thread=False)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS user_keys (
               user_id   TEXT PRIMARY KEY,
               groq_key  TEXT DEFAULT '',
               tavily_key TEXT DEFAULT ''
           )"""
    )
    conn.commit()
    return conn

_key_conn = _get_key_conn()


def save_user_keys(user_id: str, groq_key: str = "", tavily_key: str = "") -> None:
    """Upsert API keys for a user."""
    _key_conn.execute(
        """INSERT INTO user_keys (user_id, groq_key, tavily_key)
           VALUES (?, ?, ?)
           ON CONFLICT(user_id) DO UPDATE SET
               groq_key   = excluded.groq_key,
               tavily_key = excluded.tavily_key""",
        (user_id, groq_key.strip(), tavily_key.strip()),
    )
    _key_conn.commit()


def load_user_keys(user_id: str) -> dict:
    """Return {'groq_key': ..., 'tavily_key': ...} for a user (empty strings if not set)."""
    row = _key_conn.execute(
        "SELECT groq_key, tavily_key FROM user_keys WHERE user_id = ?", (user_id,)
    ).fetchone()
    if row:
        return {"groq_key": row[0] or "", "tavily_key": row[1] or ""}
    return {"groq_key": "", "tavily_key": ""}


def user_has_keys(user_id: str) -> bool:
    keys = load_user_keys(user_id)
    return bool(keys["groq_key"])


# ---------------------------------------------------------------------------
# 1. LLM factory — returns an LLM for a specific user's keys
# ---------------------------------------------------------------------------

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Build the shared college knowledge-base index once at startup.
# This is a no-op (with a warning) if college_data/ has no .md files yet.
build_college_index(embeddings)

def get_llm(user_id: str) -> ChatGroq:
    """Return a ChatGroq instance using the user's stored key (falls back to .env)."""
    keys = load_user_keys(user_id)
    api_key = keys["groq_key"] or os.getenv("GROQ_API_KEY", "")
    return ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)


def get_search_tool(user_id: str) -> TavilySearchResults:
    keys = load_user_keys(user_id)
    tavily_key = keys["tavily_key"] or os.getenv("TAVILY_API_KEY", "")
    # TavilySearchResults reads from env; set it temporarily
    os.environ["TAVILY_API_KEY"] = tavily_key
    return TavilySearchResults(max_results=3)


# Default LLM — created lazily so module import doesn't fail when the key
# isn't set yet (Streamlit Cloud loads secrets after import).
_default_llm_instance = None

def _get_default_llm() -> ChatGroq:
    global _default_llm_instance
    if _default_llm_instance is None:
        _default_llm_instance = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY", ""),
        )
    return _default_llm_instance


# ---------------------------------------------------------------------------
# 2. Universal file → Markdown converter
# ---------------------------------------------------------------------------

def _pdf_to_markdown(file_bytes: bytes) -> str:
    from pypdf import PdfReader
    reader = PdfReader(io.BytesIO(file_bytes))
    parts = []
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if text.strip():
            parts.append(f"## Page {i}\n\n{text.strip()}")
    return "\n\n---\n\n".join(parts)


def _docx_to_markdown(file_bytes: bytes) -> str:
    from docx import Document as DocxDocument
    doc = DocxDocument(io.BytesIO(file_bytes))
    lines = []
    for para in doc.paragraphs:
        style = para.style.name.lower()
        text = para.text.strip()
        if not text:
            lines.append("")
            continue
        if "heading 1" in style:
            lines.append(f"# {text}")
        elif "heading 2" in style:
            lines.append(f"## {text}")
        elif "heading 3" in style:
            lines.append(f"### {text}")
        else:
            lines.append(text)
    for table in doc.tables:
        if not table.rows:
            continue
        header = [cell.text.strip() for cell in table.rows[0].cells]
        lines.append("\n| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * len(header)) + " |")
        for row in table.rows[1:]:
            cells = [cell.text.strip() for cell in row.cells]
            lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def _pptx_to_markdown(file_bytes: bytes) -> str:
    from pptx import Presentation
    prs = Presentation(io.BytesIO(file_bytes))
    parts = []
    for i, slide in enumerate(prs.slides, 1):
        slide_lines = [f"## Slide {i}"]
        for shape in slide.shapes:
            if hasattr(shape, "text") and shape.text.strip():
                slide_lines.append(shape.text.strip())
        parts.append("\n\n".join(slide_lines))
    return "\n\n---\n\n".join(parts)


def _xlsx_to_markdown(file_bytes: bytes) -> str:
    import pandas as pd
    xl = pd.ExcelFile(io.BytesIO(file_bytes))
    parts = []
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        md_table = df.to_markdown(index=False)
        parts.append(f"## Sheet: {sheet}\n\n{md_table}")
    return "\n\n---\n\n".join(parts)


def _csv_to_markdown(file_bytes: bytes) -> str:
    import pandas as pd
    df = pd.read_csv(io.BytesIO(file_bytes))
    return df.to_markdown(index=False)


def _image_to_markdown(file_bytes: bytes, filename: str) -> str:
    try:
        import pytesseract
        from PIL import Image
        img = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(img).strip()
        return f"## Extracted text from `{filename}`\n\n{text}" if text else f"*(No text found in `{filename}`)*"
    except Exception as e:
        return f"*(Image OCR failed: {e})*"


def _txt_to_markdown(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="replace")


def convert_file_to_markdown(file_bytes: bytes, filename: str) -> tuple[str, str]:
    ext = os.path.splitext(filename.lower())[1]
    if ext == ".pdf":
        return _pdf_to_markdown(file_bytes), "pdf"
    elif ext == ".docx":
        return _docx_to_markdown(file_bytes), "docx"
    elif ext == ".pptx":
        return _pptx_to_markdown(file_bytes), "pptx"
    elif ext in (".xlsx", ".xls"):
        return _xlsx_to_markdown(file_bytes), "xlsx"
    elif ext == ".csv":
        return _csv_to_markdown(file_bytes), "csv"
    elif ext in (".txt", ".md", ".log", ".py", ".js", ".ts", ".json"):
        return _txt_to_markdown(file_bytes), "text"
    elif ext in (".png", ".jpg", ".jpeg", ".webp", ".gif"):
        return _image_to_markdown(file_bytes, filename), "image"
    else:
        return _txt_to_markdown(file_bytes), "unknown"


# ---------------------------------------------------------------------------
# 3. Per-thread retriever store
# ---------------------------------------------------------------------------
_THREAD_RETRIEVERS: Dict[str, Any] = {}
_THREAD_METADATA: Dict[str, dict] = {}
_THREAD_TITLES: Dict[str, str] = {}


def _get_retriever(thread_id: Optional[str]):
    if thread_id and thread_id in _THREAD_RETRIEVERS:
        return _THREAD_RETRIEVERS[thread_id]
    return None


def ingest_file(file_bytes: bytes, thread_id: str, filename: Optional[str] = None) -> dict:
    if not file_bytes:
        raise ValueError("No bytes received for ingestion.")
    fname = filename or "uploaded_file"
    markdown_text, file_type = convert_file_to_markdown(file_bytes, fname)
    if not markdown_text.strip():
        raise ValueError(f"Could not extract any text from `{fname}`.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", " ", ""]
    )
    raw_docs = [Document(page_content=markdown_text, metadata={"source": fname})]
    chunks = splitter.split_documents(raw_docs)
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 4}
    )
    _THREAD_RETRIEVERS[str(thread_id)] = retriever
    meta = {
        "filename": fname,
        "file_type": file_type,
        "chunks": len(chunks),
        "char_count": len(markdown_text),
    }
    _THREAD_METADATA[str(thread_id)] = meta
    return meta


# Backward-compat alias
def ingest_pdf(file_bytes: bytes, thread_id: str, filename: Optional[str] = None) -> dict:
    return ingest_file(file_bytes, thread_id, filename)


# ---------------------------------------------------------------------------
# 4. Thread title helpers
# ---------------------------------------------------------------------------

def set_thread_title(thread_id: str, title: str):
    _THREAD_TITLES[thread_id] = title


def get_thread_title(thread_id: str) -> str:
    return _THREAD_TITLES.get(thread_id, "")


def generate_chat_title(first_message: str, user_id: str = "") -> str:
    try:
        llm_instance = get_llm(user_id) if user_id else _get_default_llm()
        response = llm_instance.invoke(
            [
                SystemMessage(content=(
                    "You are a chat title generator. "
                    "Given the user's first message, respond with ONLY a short title "
                    "of 3–5 words. No punctuation, no quotes, no explanation."
                )),
                {"role": "user", "content": first_message},
            ]
        )
        title = response.content.strip().strip('"').strip("'")
        words = title.split()
        return " ".join(words[:6]) if words else "New Chat"
    except Exception:
        short = first_message.strip()[:40]
        return short + ("…" if len(first_message) > 40 else "")


# ---------------------------------------------------------------------------
# 5. LangGraph tools
# ---------------------------------------------------------------------------

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """Perform a basic arithmetic operation. Supported: add, sub, mul, div"""
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        return {"first_num": first_num, "second_num": second_num,
                "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}


@tool
def get_stock_price(symbol: str) -> dict:
    """Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') using Yahoo Finance."""
    ticker = yf.Ticker(symbol)
    info = ticker.fast_info
    return {"symbol": symbol, "current_price": info.last_price, "currency": info.currency}


@tool
def rag_tool(query: str, thread_id: Optional[str] = None) -> dict:
    """Retrieve relevant information from the uploaded document for this chat thread.
    Always include the thread_id when calling this tool."""
    retriever = _get_retriever(thread_id)
    if retriever is None:
        return {"error": "No document indexed for this chat. Upload a file first.", "query": query}
    result = retriever.invoke(query)
    return {
        "query": query,
        "context": [doc.page_content for doc in result],
        "metadata": [doc.metadata for doc in result],
        "source_file": _THREAD_METADATA.get(str(thread_id), {}).get("filename"),
    }


@tool
def college_rag_tool(query: str) -> dict:
    """Search the college knowledge base (all semesters, lecture notes, syllabus, past papers).
    Use this for ANY question about subjects, topics, exams, or coursework
    — even when no user file has been uploaded."""
    return college_rag_search(query)


# ---------------------------------------------------------------------------
# 6. Graph builder — built fresh per user_id so each user's LLM key is used
# ---------------------------------------------------------------------------

_COMPILED_GRAPHS: Dict[str, Any] = {}

conn = sqlite3.connect(":memory:", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)


def get_chatbot(user_id: str):
    """Return (or lazily create) a compiled graph that uses this user's API keys."""
    if user_id in _COMPILED_GRAPHS:
        return _COMPILED_GRAPHS[user_id]

    user_llm = get_llm(user_id)
    user_search = get_search_tool(user_id)
    user_tools = [get_stock_price, user_search, calculator, rag_tool, college_rag_tool]
    user_llm_with_tools = user_llm.bind_tools(user_tools)

    class ChatState(TypedDict):
        messages: Annotated[List[BaseMessage], add_messages]

    def chat_node(state: ChatState, config=None):
        thread_id = None
        if config and isinstance(config, dict):
            thread_id = config.get("configurable", {}).get("thread_id")

        college_kb_status = (
            "The college knowledge base is loaded and ready."
            if college_index_ready()
            else "The college knowledge base has no data yet (no .md files in college_data/)."
        )

        system_message = SystemMessage(content=(
            "You are a helpful assistant for GITAM University students. "
            f"{college_kb_status} "
            "For questions about subjects, topics, exams, or coursework, "
            "ALWAYS call `college_rag_tool` first — it searches all semester notes. "
            "For questions about the user's uploaded document, call `rag_tool` with "
            f"thread_id `{thread_id}`. "
            "You can also use web search, stock price, and calculator tools when helpful. "
            "If the user asks about a topic and the college knowledge base has no relevant "
            "result, say so and optionally do a web search."
        ))
        response = user_llm_with_tools.invoke(
            [system_message, *state["messages"]], config=config
        )
        return {"messages": [response]}

    tool_node = ToolNode(user_tools)
    graph = StateGraph(ChatState)
    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    compiled = graph.compile(checkpointer=checkpointer)
    _COMPILED_GRAPHS[user_id] = compiled
    return compiled


def invalidate_graph(user_id: str):
    """Call this after saving new keys so the next request rebuilds the graph."""
    _COMPILED_GRAPHS.pop(user_id, None)


# Legacy single chatbot (no-op — use get_chatbot(user_id) instead)
chatbot = None  # kept so old imports don't explode; frontend uses get_chatbot()


# ---------------------------------------------------------------------------
# 7. Thread utilities
# ---------------------------------------------------------------------------

def retrieve_user_threads(user_id: str) -> list:
    user_threads = []
    for checkpoint in checkpointer.list(None):
        thread_id = checkpoint.config["configurable"]["thread_id"]
        if thread_id.startswith(f"{user_id}::"):
            if thread_id not in user_threads:
                user_threads.append(thread_id)
    return user_threads


def thread_has_document(thread_id: str) -> bool:
    return str(thread_id) in _THREAD_RETRIEVERS


def thread_document_metadata(thread_id: str) -> dict:
    return _THREAD_METADATA.get(str(thread_id), {})


# ---------------------------------------------------------------------------
# 8. College knowledge base helpers (re-exported for frontend convenience)
# ---------------------------------------------------------------------------
def get_college_kb_meta() -> dict:
    """Return stats about the loaded college knowledge base index."""
    return get_college_index_meta()


def is_college_kb_ready() -> bool:
    return college_index_ready()
