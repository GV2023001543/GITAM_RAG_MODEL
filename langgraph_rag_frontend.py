import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import uuid

from langgraph_rag_backend import (
    get_chatbot,
    invalidate_graph,
    ingest_file,
    retrieve_user_threads,
    thread_document_metadata,
    generate_chat_title,
    get_thread_title,
    set_thread_title,
    save_user_keys,
    load_user_keys,
    user_has_keys,
    get_college_kb_meta,
    is_college_kb_ready,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SUPPORTED_TYPES = ["pdf", "docx", "pptx", "xlsx", "xls", "csv", "txt",
                   "md", "png", "jpg", "jpeg", "webp"]

TYPE_LABELS = {
    "pdf": "PDF", "docx": "Word", "pptx": "PowerPoint",
    "xlsx": "Excel", "xls": "Excel (legacy)", "csv": "CSV",
    "txt": "Text", "md": "Markdown",
    "png": "Image", "jpg": "Image", "jpeg": "Image", "webp": "Image",
}

# ---------------------------------------------------------------------------
# Page config — MUST be first Streamlit call
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Multi Utility Chatbot",
    page_icon="🤖",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def generate_thread_id():
    return f"{st.session_state['user_id']}::{uuid.uuid4()}"


def display_thread_label(thread_id: str) -> str:
    title = get_thread_title(thread_id)
    if title:
        return title
    parts = thread_id.split("::")
    short = parts[-1][:8] if len(parts) > 1 else thread_id[:8]
    return f"Chat {short}…"


def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(thread_id)
    st.session_state["message_history"] = []
    st.session_state["title_generated"] = False


def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)


def load_conversation(thread_id):
    bot = get_chatbot(st.session_state["user_id"])
    state = bot.get_state(config={"configurable": {"thread_id": thread_id}})
    return state.values.get("messages", [])


# ---------------------------------------------------------------------------
# Session initialisation
# ---------------------------------------------------------------------------
# user_id is persisted in the URL query string (?uid=...) so it survives
# page refreshes. On first visit a new UUID is generated and written to the
# URL; on every subsequent visit (or refresh) the same UUID is read back.

if "user_id" not in st.session_state:
    uid_from_url = st.query_params.get("uid", "")
    if uid_from_url:
        st.session_state["user_id"] = uid_from_url
    else:
        new_uid = str(uuid.uuid4())
        st.session_state["user_id"] = new_uid
        st.query_params["uid"] = new_uid

# Always keep the URL in sync (handles browser back/forward edge cases)
st.query_params["uid"] = st.session_state["user_id"]

user_id = st.session_state["user_id"]

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retrieve_user_threads(user_id)

if "ingested_docs" not in st.session_state:
    st.session_state["ingested_docs"] = {}

if "title_generated" not in st.session_state:
    st.session_state["title_generated"] = False

if "show_api_modal" not in st.session_state:
    st.session_state["show_api_modal"] = False

add_thread(st.session_state["thread_id"])

thread_key = str(st.session_state["thread_id"])
thread_docs = st.session_state["ingested_docs"].setdefault(thread_key, {})
threads = st.session_state["chat_threads"][::-1]
selected_thread = None

# ---------------------------------------------------------------------------
# API Key Modal (st.dialog)
# ---------------------------------------------------------------------------

@st.dialog("🔑 Add API Keys", width="large")
def api_key_dialog():
    existing = load_user_keys(user_id)

    st.markdown(
        "Your keys are stored **only for your session** (tied to your browser). "
        "They are never shared with other users."
    )
    st.markdown("---")

    # Groq
    st.markdown("#### Groq API Key")
    st.caption("Used for the LLM (llama-3.3-70b-versatile). Get yours at [console.groq.com](https://console.groq.com/keys).")
    groq_placeholder = "gsk_••••••••" if existing["groq_key"] else "gsk_..."
    new_groq = st.text_input(
        "Groq API Key",
        value="",
        placeholder=groq_placeholder,
        type="password",
        label_visibility="collapsed",
    )

    st.markdown("#### Tavily Search API Key")
    st.caption("Used for web search. Get yours at [app.tavily.com](https://app.tavily.com).")
    tavily_placeholder = "tvly-••••••••" if existing["tavily_key"] else "tvly-..."
    new_tavily = st.text_input(
        "Tavily API Key",
        value="",
        placeholder=tavily_placeholder,
        type="password",
        label_visibility="collapsed",
    )

    # Show masked status of currently saved keys
    if existing["groq_key"] or existing["tavily_key"]:
        st.markdown("---")
        st.markdown("**Currently saved keys:**")
        if existing["groq_key"]:
            masked = existing["groq_key"][:6] + "••••••••" + existing["groq_key"][-4:]
            st.success(f"Groq: `{masked}`")
        else:
            st.warning("Groq: not set")
        if existing["tavily_key"]:
            masked = existing["tavily_key"][:6] + "••••••••" + existing["tavily_key"][-4:]
            st.success(f"Tavily: `{masked}`")
        else:
            st.warning("Tavily: not set")

    st.markdown("")
    col_save, col_clear, col_cancel = st.columns([2, 1.2, 1])

    with col_save:
        if st.button("💾 Save Keys", use_container_width=True, type="primary"):
            # Only update fields that were actually filled in
            groq_to_save   = new_groq.strip()   or existing["groq_key"]
            tavily_to_save = new_tavily.strip()  or existing["tavily_key"]
            save_user_keys(user_id, groq_to_save, tavily_to_save)
            invalidate_graph(user_id)   # rebuild LLM with new keys
            st.success("✅ Keys saved! The chatbot will use them from your next message.")
            st.rerun()

    with col_clear:
        if st.button("🗑 Clear Keys", use_container_width=True):
            save_user_keys(user_id, "", "")
            invalidate_graph(user_id)
            st.warning("Keys cleared. Falling back to server defaults.")
            st.rerun()

    with col_cancel:
        if st.button("Cancel", use_container_width=True):
            st.rerun()


# ---------------------------------------------------------------------------
# Top bar: title + API key button (top-right via columns)
# ---------------------------------------------------------------------------

col_title, col_btn = st.columns([8, 2])
with col_title:
    st.title("🤖 Multi Utility Chatbot")
with col_btn:
    st.markdown("<div style='padding-top:18px'>", unsafe_allow_html=True)
    has_keys = user_has_keys(user_id)
    btn_label = "🔑 API Keys ✅" if has_keys else "🔑 Add API Keys"
    btn_type  = "secondary" if has_keys else "primary"
    if st.button(btn_label, key="open_api_modal", use_container_width=True, type=btn_type):
        api_key_dialog()
    st.markdown("</div>", unsafe_allow_html=True)

# Warn if no keys set
if not has_keys:
    st.info(
        "ℹ️ No API keys saved yet. The chatbot will use the server's default keys. "
        "Click **Add API Keys** to use your own.",
        icon="ℹ️",
    )

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

st.sidebar.title("LangGraph RAG Chatbot")

if st.sidebar.button("➕ New Chat", use_container_width=True):
    reset_chat()
    st.rerun()

# Document status
if thread_docs:
    latest_doc = list(thread_docs.values())[-1]
    file_type = latest_doc.get("file_type", "file")
    label = TYPE_LABELS.get(file_type, file_type.upper())
    st.sidebar.success(
        f"📄 **{label}** · `{latest_doc.get('filename')}`  \n"
        f"{latest_doc.get('chunks')} chunks · {latest_doc.get('char_count', 0):,} chars"
    )
else:
    st.sidebar.info("No document indexed yet.")

# College Knowledge Base status
st.sidebar.markdown("---")
st.sidebar.subheader("📚 College Knowledge Base")
if is_college_kb_ready():
    kb_meta = get_college_kb_meta()
    st.sidebar.success(
        f"✅ **{len(kb_meta['files'])} file(s)** loaded · "
        f"{kb_meta['chunks']} chunks · {kb_meta['chars']:,} chars"
    )
    with st.sidebar.expander("View loaded files"):
        for f in kb_meta["files"]:
            st.markdown(f"• `{f}`")
else:
    st.sidebar.warning(
        "⚠️ No college data loaded.\n\n"
        "Add `.md` files to the `college_data/` folder and restart the app."
    )

# Universal file uploader
st.sidebar.markdown("**Upload a document for this chat**")
st.sidebar.caption("Supported: PDF, Word, PowerPoint, Excel, CSV, Text, Markdown, Images")
uploaded_file = st.sidebar.file_uploader(
    "Choose a file", type=SUPPORTED_TYPES, label_visibility="collapsed"
)

if uploaded_file:
    if uploaded_file.name in thread_docs:
        st.sidebar.info(f"`{uploaded_file.name}` already processed for this chat.")
    else:
        with st.sidebar.status("Converting & indexing…", expanded=True) as status_box:
            try:
                summary = ingest_file(
                    uploaded_file.getvalue(),
                    thread_id=thread_key,
                    filename=uploaded_file.name,
                )
                thread_docs[uploaded_file.name] = summary
                file_label = TYPE_LABELS.get(summary.get("file_type", ""), "File")
                status_box.update(
                    label=f"✅ {file_label} indexed ({summary['chunks']} chunks)",
                    state="complete", expanded=False,
                )
            except Exception as exc:
                status_box.update(
                    label=f"❌ Indexing failed: {exc}", state="error", expanded=True
                )

# Past conversations
st.sidebar.markdown("---")
st.sidebar.subheader("Past conversations")
if not threads:
    st.sidebar.write("No past conversations yet.")
else:
    for tid in threads:
        label = display_thread_label(tid)
        btn_label_side = f"▶ {label}" if tid == thread_key else label
        if st.sidebar.button(btn_label_side, key=f"side-thread-{tid}", use_container_width=True):
            selected_thread = tid

# ---------------------------------------------------------------------------
# Main chat area
# ---------------------------------------------------------------------------

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Ask about your document or use tools…")

if user_input:
    # Auto-generate a chat title on the very first message
    if not st.session_state["title_generated"] and not get_thread_title(thread_key):
        title = generate_chat_title(user_input, user_id=user_id)
        set_thread_title(thread_key, title)
        st.session_state["title_generated"] = True

    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    CONFIG = {
        "configurable": {"thread_id": thread_key},
        "metadata": {"thread_id": thread_key},
        "run_name": "chat_turn",
    }

    chatbot = get_chatbot(user_id)

    with st.chat_message("assistant"):
        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, _ in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running", expanded=True,
                        )
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message}
    )

    doc_meta = thread_document_metadata(thread_key)
    if doc_meta:
        file_label = TYPE_LABELS.get(doc_meta.get("file_type", ""), "Document")
        st.caption(
            f"{file_label} indexed: {doc_meta.get('filename')} · "
            f"chunks: {doc_meta.get('chunks')} · "
            f"chars: {doc_meta.get('char_count', 0):,}"
        )

st.divider()

# ---------------------------------------------------------------------------
# Load a past thread when user clicks it in sidebar
# ---------------------------------------------------------------------------
if selected_thread:
    st.session_state["thread_id"] = selected_thread
    messages = load_conversation(selected_thread)
    temp_messages = []
    for msg in messages:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        temp_messages.append({"role": role, "content": msg.content})
    st.session_state["message_history"] = temp_messages
    st.session_state["ingested_docs"].setdefault(str(selected_thread), {})
    st.session_state["title_generated"] = bool(get_thread_title(selected_thread))
    st.rerun()