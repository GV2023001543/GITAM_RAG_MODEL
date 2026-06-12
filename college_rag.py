"""
college_rag.py
--------------
Shared, always-on RAG over the college knowledge base.

📁 Drop your semester .md files inside:
    college_data/
        sem1_maths.md
        sem2_os.md
        sem3_dbms.md
        ...

This module is imported once at startup. The FAISS index is built from every
.md file found in college_data/ and is shared across ALL users/threads.
"""

from __future__ import annotations

import os
import glob
import logging
from typing import Optional

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
COLLEGE_DATA_DIR = os.path.join(os.path.dirname(__file__), "college_data")
CHUNK_SIZE       = 1000
CHUNK_OVERLAP    = 200
TOP_K            = 5          # how many chunks to return per query

# ---------------------------------------------------------------------------
# Internal state
# ---------------------------------------------------------------------------
_college_retriever = None      # set once at build time
_college_index_meta: dict = {  # stats shown in the UI
    "files": [],
    "chunks": 0,
    "chars": 0,
}


def _load_md_files(data_dir: str) -> list[Document]:
    """Read every .md file in data_dir into LangChain Documents."""
    pattern = os.path.join(data_dir, "**", "*.md")
    paths = glob.glob(pattern, recursive=True)
    if not paths:
        logger.warning(
            "college_rag: no .md files found in %s — college RAG disabled.", data_dir
        )
        return []

    docs = []
    for path in sorted(paths):
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
            rel = os.path.relpath(path, data_dir)
            docs.append(Document(page_content=text, metadata={"source": rel}))
            logger.info("college_rag: loaded %s (%d chars)", rel, len(text))
        except Exception as exc:
            logger.error("college_rag: failed to read %s — %s", path, exc)
    return docs


def build_college_index(embeddings) -> None:
    """
    Build (or rebuild) the shared FAISS index from college_data/*.md files.
    Call this once at app startup, passing the shared embeddings model.

    Example usage in langgraph_rag_backend.py:
        from college_rag import build_college_index, college_rag_search
        build_college_index(embeddings)          # call at module level
    """
    global _college_retriever, _college_index_meta

    raw_docs = _load_md_files(COLLEGE_DATA_DIR)
    if not raw_docs:
        _college_retriever = None
        _college_index_meta = {"files": [], "chunks": 0, "chars": 0}
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(raw_docs)
    vector_store = FAISS.from_documents(chunks, embeddings)
    _college_retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K},
    )

    total_chars = sum(len(d.page_content) for d in raw_docs)
    _college_index_meta = {
        "files": [d.metadata["source"] for d in raw_docs],
        "chunks": len(chunks),
        "chars": total_chars,
    }
    logger.info(
        "college_rag: index ready — %d files, %d chunks, %d chars",
        len(raw_docs), len(chunks), total_chars,
    )


def college_rag_search(query: str) -> dict:
    """
    Run a similarity search against the college knowledge base.
    Returns a dict with 'context' (list of strings) or 'error'.
    """
    if _college_retriever is None:
        return {
            "error": (
                "College knowledge base is not available. "
                "No .md files found in college_data/ folder."
            ),
            "query": query,
        }
    results = _college_retriever.invoke(query)
    return {
        "query": query,
        "context": [doc.page_content for doc in results],
        "sources": [doc.metadata.get("source", "unknown") for doc in results],
    }


def get_college_index_meta() -> dict:
    """Return stats about the loaded college index (for the UI)."""
    return dict(_college_index_meta)


def college_index_ready() -> bool:
    return _college_retriever is not None