"""
langgraph_rag_frontend.py — TeamDino RAG Model
Tabs: Chat | Cheat Sheet | Flashcards | Explain Concept | Summary | Diagram | Export
Theme: gray background, black text only.
"""
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import uuid, datetime

from langgraph_rag_backend import (
    get_chatbot, invalidate_graph, ingest_file,
    retrieve_user_threads, thread_document_metadata,
    generate_chat_title, get_thread_title, set_thread_title,
    save_user_keys, load_user_keys, user_has_keys,
    get_college_kb_meta, is_college_kb_ready,
    MissingAPIKeyError,
    generate_cheat_sheet, detect_subject_unit,
    generate_flashcards, explain_concept, summarise_topic,
    explain_diagram_image,
    export_conversation_txt,
)

# ── Branding & palette (gray + black only) ────────────────────────────────────
BRAND     = "TeamDino RAG Model"
TEXT      = "#111111"   # black text
TEXT_DIM  = "#444444"   # dim gray text
BG        = "#d9d9d9"   # gray background
SURFACE   = "#e9e9e9"   # raised gray
SURFACE_2 = "#f5f5f5"   # card gray
BORDER    = "#b3b3b3"   # gray border

SUPPORTED_TYPES = ["pdf", "docx", "pptx", "xlsx", "xls", "csv", "txt", "md"]
TYPE_LABELS = {"pdf": "PDF", "docx": "Word", "pptx": "PowerPoint", "xlsx": "Excel",
               "xls": "Excel", "csv": "CSV", "txt": "Text", "md": "Markdown"}

st.set_page_config(page_title=BRAND, page_icon="data:image/png;base64,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", layout="wide",
                   initial_sidebar_state="collapsed")

# ── CSS (token approach: single-brace CSS, swapped via .replace) ──────────────
CSS = """
<style>
/* Hide non-essential Streamlit chrome, but keep menu and sidebar controls visible. */
footer, .stDeployButton, [data-testid="stDeployButton"],
[data-testid="stAppDeployButton"], [data-testid="deployButton"],
button[title="Deploy"], button[aria-label="Deploy"],
[data-testid="manage-app-button"],
a[href*="github"], #stDecoration { display:none !important; visibility:hidden !important; }

/* Keep Streamlit's header/menu area visible for the hamburger and sidebar toggle. */
header, #MainMenu, [data-testid="stMainMenu"] {
  display: block !important;
  visibility: visible !important;
}
header {
  background: transparent !important;
  z-index: 1000 !important;
}
[data-testid="stToolbar"] {
  display: flex !important;
  visibility: visible !important;
  z-index: 1001 !important;
}

/* Hamburger menu button styling */
[data-testid="stToolbar"] button { color: #111111 !important; }
[data-testid="stToolbar"] button svg { stroke: #111111 !important; fill: #111111 !important; }
[data-testid="stToolbar"] svg { stroke: #111111 !important; fill: #111111 !important; color: #111111 !important; }

/* Ensure sidebar is visible and accessible */
[data-testid="stSidebarNav"] { display: flex !important; visibility: visible !important; }
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
  z-index: 1002 !important;
}
button[aria-label="Toggle sidebar"],
button[aria-label="Open sidebar"],
button[aria-label="Close sidebar"],
button[kind="header"] {
  display: flex !important;
  visibility: visible !important;
  opacity: 1 !important;
  color: #111111 !important;
  background: #f5f5f5 !important;
  border: 1px solid __BORDER__ !important;
  z-index: 1002 !important;
}
[data-testid="stSidebarCollapseButton"] svg,
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="collapsedControl"] svg,
button[aria-label="Toggle sidebar"] svg,
button[aria-label="Open sidebar"] svg,
button[aria-label="Close sidebar"] svg {
  stroke: #111111 !important;
  fill: #111111 !important;
}

/* ── Base theme ── */
[data-testid="stAppViewContainer"] { background: __BG__; color: __TEXT__ !important; }
[data-testid="stSidebar"] {
  background: __SURFACE__; border-right: 1px solid __BORDER__; color: __TEXT__ !important;
}

/* ── Sidebar elements ── */
[data-testid="stSidebar"] * { color: __TEXT__ !important; }
[data-testid="stSidebar"] button { background: #808080; color: #111111 !important; border: 1px solid __BORDER__; }
[data-testid="stSidebar"] label { color: __TEXT__ !important; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: __TEXT__ !important; }
[data-testid="stSidebar"] input { background: __SURFACE_2__; color: __TEXT__ !important; border: 1px solid __BORDER__; }
[data-testid="stSidebar"] input::placeholder { color: __TEXT_DIM__ !important; }
[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"] { border: 2px dashed __BORDER__; background: __SURFACE_2__; }
[data-testid="stSidebar"] .stExpander { border: 1px solid __BORDER__; }
[data-testid="stSidebar"] .stExpander > summary { color: __TEXT__ !important; }
[data-testid="stSidebar"] .stRadio { color: __TEXT__ !important; }
[data-testid="stSidebar"] .stCheckbox { color: __TEXT__ !important; }

/* ── Global black text ── */
[data-testid="stAppViewContainer"] p,
[data-testid="stAppViewContainer"] li,
[data-testid="stAppViewContainer"] span,
[data-testid="stAppViewContainer"] label,
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] * { color: __TEXT__ !important; }
h1,h2,h3,h4,h5,h6 { color: __TEXT__ !important; }
[data-testid="stCaptionContainer"], small { color: __TEXT_DIM__ !important; }

/* ── Brand header ── */
.td-brand {
  display:flex; align-items:center; gap:14px; padding:14px 20px; margin-bottom:6px;
  background: __SURFACE_2__; border:1px solid __BORDER__; border-radius:18px;
  box-shadow: 0 4px 14px -8px #00000033;
}
.td-logo {
  width:46px; height:46px; border-radius:14px; display:grid; place-items:center;
  background: transparent; box-shadow: none;
}
.td-logo span { font-size:26px; color:__SURFACE_2__; font-weight:800; }
.td-logo img { display:none; }
.td-logo::before {
  content:""; width:46px; height:46px; display:block;
  background: center / contain no-repeat url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 256 256'%3E%3Cg fill='none' stroke='%23000' stroke-width='22' stroke-linecap='round'%3E%3Cline x1='128' y1='128' x2='128' y2='38'/%3E%3Cline x1='128' y1='128' x2='128' y2='218'/%3E%3Cline x1='128' y1='128' x2='50' y2='83'/%3E%3Cline x1='128' y1='128' x2='206' y2='83'/%3E%3Cline x1='128' y1='128' x2='50' y2='173'/%3E%3Cline x1='128' y1='128' x2='206' y2='173'/%3E%3C/g%3E%3Cg fill='%23fff' stroke='%23000' stroke-width='22'%3E%3Ccircle cx='128' cy='128' r='39'/%3E%3Ccircle cx='128' cy='38' r='20'/%3E%3Ccircle cx='128' cy='218' r='20'/%3E%3Ccircle cx='50' cy='83' r='20'/%3E%3Ccircle cx='206' cy='83' r='20'/%3E%3Ccircle cx='50' cy='173' r='20'/%3E%3Ccircle cx='206' cy='173' r='20'/%3E%3C/g%3E%3C/svg%3E");
}
.td-title-row { display:flex; align-items:center; gap:8px; }
.td-mini-favicon {
  width:28px; height:28px; display:inline-grid; place-items:center;
  background: transparent; overflow:visible;
  line-height:1; flex:0 0 auto;
}
.td-mini-favicon svg { width:100%; height:100%; display:block; }
.td-title { font-size:1.45rem; font-weight:800; letter-spacing:-0.02em; color:__TEXT__ !important; }
.td-sub { font-size:.8rem; color:__TEXT_DIM__ !important; margin-top:-2px; }

/* ── Cards ── */
.td-card {
  background: __SURFACE_2__; border:1px solid __BORDER__; border-radius:16px;
  padding:18px 20px; margin:8px 0; box-shadow: 0 4px 16px -10px #00000033;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] { gap:6px; overflow-x:auto; flex-wrap:nowrap;
  scrollbar-width:none; border-bottom:1px solid __BORDER__; }
.stTabs [data-baseweb="tab-list"]::-webkit-scrollbar { display:none; }
.stTabs [data-baseweb="tab"] {
  background:__SURFACE__; border:1px solid __BORDER__; border-radius:12px 12px 0 0;
  padding:8px 16px; color:__TEXT_DIM__ !important; font-weight:600;
}
.stTabs [aria-selected="true"] {
  background: __SURFACE_2__; color:__TEXT__ !important; border-bottom:2px solid __TEXT__;
}

/* ── Chat bubbles ── */
[data-testid="stChatMessage"] {
  border-radius:16px; padding:6px 14px; margin-bottom:10px; border:1px solid __BORDER__;
  background: __SURFACE_2__; box-shadow:0 4px 14px -10px #00000026;
}
[data-testid="stChatMessage"] * { color:__TEXT__ !important; }

/* ── Buttons ── */
.stButton > button {
  border-radius:12px; font-weight:600; border:1px solid __BORDER__;
  background: #808080; /* gray */
  color: #111111; /* black text */
  transition:transform .08s ease, box-shadow .12s ease;
  box-shadow:0 3px 8px -5px #00000040;
}
.stButton > button:hover { transform:translateY(-1px);
  box-shadow:0 6px 14px -8px #00000059; border-color:__TEXT__; }
.stButton > button:active { transform:translateY(1px); }
.stButton > button[kind="primary"] {
  background: #808080; color:__SURFACE_2__ !important; border-color:#808080;
  box-shadow:0 6px 14px -8px #00000059;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
  background:__SURFACE_2__; border:1px solid __BORDER__; border-radius:16px;
  box-shadow:0 4px 14px -10px #00000033;
}
[data-testid="stChatInput"] textarea { color:__TEXT__ !important; -webkit-text-fill-color:__TEXT__ !important; }
[data-testid="stChatInput"] textarea::placeholder { color:__TEXT_DIM__ !important; }

/* ── Inputs ── */
[data-testid="stTextInput"] input, [data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea {
  background:__SURFACE_2__; border:1px solid __BORDER__; border-radius:10px;
  color:__TEXT__ !important; -webkit-text-fill-color:__TEXT__ !important;
}
[data-testid="stTextInput"] input::placeholder { color:__TEXT_DIM__ !important; }

/* ── Radio ── */
[data-testid="stRadio"] label, [data-baseweb="radio"] { color:__TEXT__ !important; }

/* ── Flashcards ── */
.fc-grid { display:flex; flex-wrap:wrap; gap:14px; }
.fc-card {
  background: __SURFACE_2__; border:1px solid __BORDER__; border-radius:14px;
  padding:16px 18px; flex:1 1 280px; min-width:240px; box-shadow:0 4px 16px -12px #00000033;
}
.fc-q { color:__TEXT__ !important; font-weight:700; margin-bottom:6px; font-size:.94em; }
.fc-a { color:__TEXT_DIM__ !important; font-size:.9em; border-top:1px solid __BORDER__;
  padding-top:8px; margin-top:8px; }

/* ── Badges ── */
.subj-badge { background:__SURFACE_2__; padding:6px 14px; border-radius:999px;
  font-size:.8em; color:__TEXT__ !important; margin-bottom:8px; display:inline-block;
  border:1px solid __BORDER__; }

@media (max-width:768px) {
  [data-testid="stSidebar"] { width:100% !important; min-width:unset !important; }
  .block-container { padding:.5rem .75rem !important; }
  .td-title { font-size:1.15rem !important; }
  .stTabs [data-baseweb="tab"] { font-size:.72rem !important; padding:6px 10px !important; }
}
</style>
"""
for _token, _val in {
    "__TEXT_DIM__": TEXT_DIM, "__TEXT__": TEXT, "__BG__": BG,
    "__SURFACE_2__": SURFACE_2, "__SURFACE__": SURFACE, "__BORDER__": BORDER,
}.items():
    CSS = CSS.replace(_token, _val)
st.markdown(CSS, unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
def generate_thread_id():
    return f"{st.session_state['user_id']}::{uuid.uuid4()}"

def display_thread_label(tid):
    t = get_thread_title(tid)
    if t: return t
    parts = tid.split("::")
    return f"Chat {parts[-1][:8]}…" if len(parts) > 1 else f"Chat {tid[:8]}…"

def reset_chat():
    tid = generate_thread_id()
    st.session_state.update({"thread_id": tid, "message_history": [],
                             "title_generated": False, "last_detected": {}})
    add_thread(tid)

def add_thread(tid):
    if tid not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(tid)

def _clean_history(msgs):
    """Keep only real user questions and final assistant answers.
    Drops ToolMessages and tool-call-only AIMessages so raw '{query:...}'
    payloads never show when switching chats."""
    cleaned = []
    for m in msgs:
        if isinstance(m, ToolMessage):
            continue
        if isinstance(m, HumanMessage):
            content = (m.content or "").strip()
            if content:
                cleaned.append({"role": "user", "content": content})
        elif isinstance(m, AIMessage):
            if getattr(m, "tool_calls", None) and not (m.content or "").strip():
                continue
            content = (m.content or "").strip()
            if content:
                cleaned.append({"role": "assistant", "content": content})
    return cleaned

def load_conversation(tid):
    bot = get_chatbot(st.session_state["user_id"])
    s = bot.get_state(config={"configurable": {"thread_id": tid}})
    return s.values.get("messages", [])

def _key_error(e):
    st.error(str(e))
    st.info("Click **API Keys** at the top right to enter your Groq key.")
    st.stop()

# ── Session init ──────────────────────────────────────────────────────────────
if "user_id" not in st.session_state:
    uid = st.query_params.get("uid", "")
    if not uid:
        uid = str(uuid.uuid4())
        st.query_params["uid"] = uid
    st.session_state["user_id"] = uid
st.query_params["uid"] = st.session_state["user_id"]
user_id = st.session_state["user_id"]

for k, v in [("message_history", []), ("title_generated", False),
             ("ingested_docs", {}), ("last_detected", {}),
             ("fc_cards", []), ("fc_flipped", set())]:
    if k not in st.session_state:
        st.session_state[k] = v

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()
if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retrieve_user_threads(user_id)

add_thread(st.session_state["thread_id"])
thread_key = str(st.session_state["thread_id"])
thread_docs = st.session_state["ingested_docs"].setdefault(thread_key, {})
threads = st.session_state["chat_threads"][::-1]
selected_thread = None

# ── API Key Dialog ────────────────────────────────────────────────────────────
@st.dialog("API Keys", width="large")
def api_key_dialog():
    ex = load_user_keys(user_id)
    st.markdown("Your keys are stored **only for your account**. Never shared.")
    st.divider()
    st.markdown("##### :material/key: Groq API Key")
    st.caption("Get yours at [console.groq.com](https://console.groq.com/keys).")
    new_groq = st.text_input("Groq", value="",
        placeholder="gsk_••••••••" if ex["groq_key"] else "gsk_...",
        type="password", label_visibility="collapsed")
    st.markdown("##### :material/travel_explore: Tavily Search API Key")
    st.caption("Get yours at [app.tavily.com](https://app.tavily.com).")
    new_tavily = st.text_input("Tavily", value="",
        placeholder="tvly-••••••••" if ex["tavily_key"] else "tvly-...",
        type="password", label_visibility="collapsed")
    if ex["groq_key"] or ex["tavily_key"]:
        st.divider()
        st.markdown("**Saved keys:**")
        if ex["groq_key"]:
            st.write(f"Groq: `{ex['groq_key'][:6]}••••{ex['groq_key'][-4:]}`")
        if ex["tavily_key"]:
            st.write(f"Tavily: `{ex['tavily_key'][:6]}••••{ex['tavily_key'][-4:]}`")
    c1, c2, c3 = st.columns([2, 1.2, 1])
    with c1:
        if st.button(":material/save: Save", use_container_width=True, type="primary"):
            save_user_keys(user_id, new_groq.strip() or ex["groq_key"],
                           new_tavily.strip() or ex["tavily_key"])
            invalidate_graph(user_id); st.rerun()
    with c2:
        if st.button(":material/delete: Clear", use_container_width=True):
            save_user_keys(user_id, "", ""); invalidate_graph(user_id); st.rerun()
    with c3:
        if st.button("Cancel", use_container_width=True):
            st.rerun()

# ── Brand header + API key button ─────────────────────────────────────────────
col_title, col_btn = st.columns([8, 2])
with col_title:
    st.markdown("""
      <div class="td-brand">
        <div class="td-logo"><img src="data:image/png;base64,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" style="width:100%; height:100%; object-fit:contain;"></div>
        <div>
          <div class="td-title">TeamDino RAG Model</div>
          <div class="td-sub">Retrieval-augmented study assistant by TeamDino</div>
        </div>
      </div>
    """, unsafe_allow_html=True)
with col_btn:
    st.markdown("<div style='padding-top:14px'>", unsafe_allow_html=True)
    has_keys = user_has_keys(user_id)
    if st.button("API Keys" if has_keys else "Add API Keys",
                 icon=":material/key:", key="open_api_modal",
                 use_container_width=True,
                 type="secondary" if has_keys else "primary"):
        api_key_dialog()
    st.markdown("</div>", unsafe_allow_html=True)
if not has_keys:
    st.info("No API keys saved — using server defaults. Click **Add API Keys** to use your own.",
            icon=":material/info:")

# ── Tabs (Chat is default / first) ────────────────────────────────────────────
tab_chat, tab_cheat, tab_fc, tab_explain, tab_summary, tab_diag, tab_export = st.tabs([
    "Chat", "Cheat Sheet", "Flashcards", "Explain", "Summary", "Diagram", "Export"])

# =============================================================================
# TAB 1 — CHAT
# =============================================================================
with tab_chat:
    st.sidebar.markdown("""
      <div class="td-brand" style="margin-bottom:12px;padding:10px 14px">
        <div>
          <div class="td-title-row">
            <span class="td-mini-favicon" aria-label="TeamDino favicon">
              <svg viewBox="0 0 256 256" role="img" aria-hidden="true">
                <g fill="none" stroke="#000000" stroke-width="22" stroke-linecap="round">
                  <line x1="128" y1="128" x2="128" y2="38" />
                  <line x1="128" y1="128" x2="128" y2="218" />
                  <line x1="128" y1="128" x2="50" y2="83" />
                  <line x1="128" y1="128" x2="206" y2="83" />
                  <line x1="128" y1="128" x2="50" y2="173" />
                  <line x1="128" y1="128" x2="206" y2="173" />
                </g>
                <g fill="#ffffff" stroke="#000000" stroke-width="22">
                  <circle cx="128" cy="128" r="39" />
                  <circle cx="128" cy="38" r="20" />
                  <circle cx="128" cy="218" r="20" />
                  <circle cx="50" cy="83" r="20" />
                  <circle cx="206" cy="83" r="20" />
                  <circle cx="50" cy="173" r="20" />
                  <circle cx="206" cy="173" r="20" />
                </g>
              </svg>
            </span>
            <div class="td-title" style="font-size:1.05rem">TeamDino</div>
          </div>
        <div class="td-sub">RAG Model</div></div>
      </div>
    """, unsafe_allow_html=True)

    if st.sidebar.button("New Chat", icon=":material/add:", use_container_width=True):
        reset_chat(); st.rerun()

    if is_college_kb_ready():
        kb = get_college_kb_meta()
        st.sidebar.info(f"Knowledge Base: **{len(kb['files'])} file(s)** · {kb['chunks']} chunks",
                        icon=":material/menu_book:")
        with st.sidebar.expander("Files"):
            for f in kb["files"]:
                st.markdown(f"• `{f}`")
    else:
        st.sidebar.info("No knowledge base data. Add `.md` files to `college_data/`.",
                        icon=":material/warning:")

    if thread_docs:
        d = list(thread_docs.values())[-1]
        lbl = TYPE_LABELS.get(d.get("file_type", ""), d.get("file_type", "").upper())
        st.sidebar.info(f"{lbl} · `{d.get('filename')}` · {d.get('chunks')} chunks",
                        icon=":material/description:")
    else:
        st.sidebar.info("No personal document uploaded.", icon=":material/upload_file:")

    st.sidebar.markdown("**Upload your document**")
    st.sidebar.caption("PDF, Word, PPT, Excel, CSV, Text, Markdown")
    up = st.sidebar.file_uploader("upload", type=SUPPORTED_TYPES, label_visibility="collapsed")
    if up:
        if up.name in thread_docs:
            st.sidebar.info(f"`{up.name}` already processed.")
        else:
            with st.sidebar.status("Indexing…", expanded=True) as sb:
                try:
                    s = ingest_file(up.getvalue(), thread_id=thread_key, filename=up.name)
                    thread_docs[up.name] = s
                    sb.update(label=f"Indexed ({s['chunks']} chunks)",
                              state="complete", expanded=False)
                except Exception as ex:
                    sb.update(label=f"Failed: {ex}", state="error", expanded=True)

    st.sidebar.divider()
    st.sidebar.subheader("Past chats")
    if not threads:
        st.sidebar.caption("No chats yet.")
    else:
        for tid in threads:
            lbl = display_thread_label(tid)
            is_active = (tid == thread_key)
            if st.sidebar.button(lbl, key=f"s-{tid}", use_container_width=True,
                                 icon=":material/chat:" if is_active else ":material/forum:"):
                selected_thread = tid

    # Subject detection badge (no colored dots — plain text)
    if st.session_state["last_detected"]:
        d = st.session_state["last_detected"]
        conf = d.get("confidence", 0)
        sem_txt = f"Sem {d['semester']} · " if d.get("semester") else ""
        st.markdown(
            f"<span class='subj-badge'>{sem_txt}<b>{d.get('subject', '?')}</b>"
            f" — {d.get('unit', '?')} &nbsp;· {int(conf * 100)}%</span>",
            unsafe_allow_html=True)

    # Render all chat messages inside one transcript area so the input stays below them.
    chat_area = st.container()
    with chat_area:
        for msg in st.session_state["message_history"]:
            avatar = ":material/person:" if msg["role"] == "user" else ":material/smart_toy:"
            with st.chat_message(msg["role"], avatar=avatar):
                st.markdown(msg["content"])

    # Chat input at bottom (after all messages)
    user_input = st.chat_input("Ask anything about your subjects…")

    if user_input:
        if not st.session_state["title_generated"] and not get_thread_title(thread_key):
            try:
                set_thread_title(thread_key, generate_chat_title(user_input, user_id))
            except MissingAPIKeyError:
                set_thread_title(thread_key, user_input[:40])
            st.session_state["title_generated"] = True

        try:
            st.session_state["last_detected"] = detect_subject_unit(user_input, user_id)
        except Exception:
            pass

        st.session_state["message_history"].append({"role": "user", "content": user_input})
        with chat_area:
            with st.chat_message("user", avatar=":material/person:"):
                st.markdown(user_input)

        CONFIG = {"configurable": {"thread_id": thread_key},
                  "metadata": {"thread_id": thread_key}, "run_name": "chat_turn"}
        try:
            chatbot = get_chatbot(user_id)
        except MissingAPIKeyError as e:
            _key_error(e)

        TOOL_LABELS = {
            "college_rag_tool": "Searching college notes…",
            "rag_tool": "Searching your document…",
            "tavily_search_results_json": "Web search…",
            "get_stock_price": "Fetching stock price…",
            "calculator": "Calculating…",
        }
        with chat_area:
            with st.chat_message("assistant", avatar=":material/smart_toy:"):
                sh = {"box": None}

                def ai_stream():
                    for chunk, _ in chatbot.stream(
                            {"messages": [HumanMessage(content=user_input)]},
                            config=CONFIG, stream_mode="messages"):
                        if isinstance(chunk, ToolMessage):
                            lbl = TOOL_LABELS.get(getattr(chunk, "name", ""),
                                                  f"Working: {getattr(chunk, 'name', '')}…")
                            if sh["box"] is None:
                                sh["box"] = st.status(lbl, expanded=True)
                            else:
                                sh["box"].update(label=lbl, state="running", expanded=True)
                        if isinstance(chunk, AIMessage) and chunk.content:
                            yield chunk.content

                ai_msg = st.write_stream(ai_stream())
                if sh["box"]:
                    sh["box"].update(label="Done", state="complete", expanded=False)

        st.session_state["message_history"].append({"role": "assistant", "content": ai_msg})

    if selected_thread:
        st.session_state["thread_id"] = selected_thread
        msgs = load_conversation(selected_thread)
        st.session_state["message_history"] = _clean_history(msgs)
        st.session_state["ingested_docs"].setdefault(str(selected_thread), {})
        st.session_state["title_generated"] = bool(get_thread_title(selected_thread))
        st.rerun()

# =============================================================================
# TAB 2 — CHEAT SHEET
# =============================================================================
with tab_cheat:
    st.subheader(":material/description: Exam Cheat Sheet")
    st.caption("Dense, exam-focused one-pager built from your course notes.")
    c1, c2 = st.columns(2)
    with c1:
        cs_sub = st.text_input("Subject", placeholder="e.g. Operating Systems", key="cs_s")
    with c2:
        cs_unit = st.text_input("Unit / Topic", placeholder="e.g. CPU Scheduling", key="cs_u")
    if st.button("Build Cheat Sheet", icon=":material/auto_awesome:", type="primary",
                 use_container_width=True, key="cs_btn"):
        if not cs_sub.strip() or not cs_unit.strip():
            st.error("Enter both subject and unit.")
        else:
            try:
                with st.spinner("Compiling from course notes…"):
                    sheet = generate_cheat_sheet(cs_sub.strip(), cs_unit.strip(), user_id)
                st.markdown("<div class='td-card'>", unsafe_allow_html=True)
                st.markdown(sheet)
                st.markdown("</div>", unsafe_allow_html=True)
                st.download_button("Download (.txt)", icon=":material/download:",
                    data=sheet.encode(),
                    file_name=f"cheatsheet_{cs_sub[:15]}_{cs_unit[:15]}.txt",
                    mime="text/plain", key="cs_dl")
            except MissingAPIKeyError as e:
                _key_error(e)

# =============================================================================
# TAB 3 — FLASHCARDS
# =============================================================================
with tab_fc:
    st.subheader(":material/style: Flashcard Generator")
    st.caption("Auto-generate Q&A flashcard pairs from your course notes.")
    c1, c2, c3 = st.columns([3, 3, 1])
    with c1:
        fc_sub = st.text_input("Subject", placeholder="e.g. DBMS", key="fc_s")
    with c2:
        fc_unit = st.text_input("Unit / Topic", placeholder="e.g. Normalization", key="fc_u")
    with c3:
        fc_n = st.number_input("Count", min_value=3, max_value=20, value=8, key="fc_n")

    col_gen, col_csv = st.columns([2, 1])
    with col_gen:
        if st.button("Generate Flashcards", icon=":material/bolt:", type="primary",
                     use_container_width=True, key="fc_btn"):
            if not fc_sub.strip() or not fc_unit.strip():
                st.error("Enter both subject and unit.")
            else:
                try:
                    with st.spinner("Generating flashcards…"):
                        cards = generate_flashcards(fc_sub.strip(), fc_unit.strip(), fc_n, user_id)
                    st.session_state["fc_cards"] = cards
                    st.session_state["fc_flipped"] = set()
                except MissingAPIKeyError as e:
                    _key_error(e)

    cards = st.session_state.get("fc_cards", [])
    if cards:
        with col_csv:
            import csv, io as _io
            buf = _io.StringIO()
            w = csv.writer(buf)
            w.writerow(["Question", "Answer"])
            for c in cards:
                w.writerow([c.get("question", ""), c.get("answer", "")])
            st.download_button("CSV (Anki)", icon=":material/download:",
                data=buf.getvalue().encode(),
                file_name=f"flashcards_{fc_sub[:10]}.csv", mime="text/csv",
                use_container_width=True, key="fc_csv")

        st.divider()
        st.caption(f"{len(cards)} cards — click a button below to reveal answers")

        cards_html = "<div class='fc-grid'>"
        flipped = st.session_state.get("fc_flipped", set())
        for i, card in enumerate(cards):
            q = card.get("question", "")
            a = card.get("answer", "")
            ans_part = f"<div class='fc-a'>{a}</div>" if i in flipped else ""
            cards_html += f"<div class='fc-card'><div class='fc-q'>Q{i+1}: {q}</div>{ans_part}</div>"
        cards_html += "</div>"
        st.markdown(cards_html, unsafe_allow_html=True)

        st.markdown("")
        cols = st.columns(min(len(cards), 5))
        for i, card in enumerate(cards):
            with cols[i % len(cols)]:
                label = f"Hide #{i+1}" if i in flipped else f"Show #{i+1}"
                if st.button(label, key=f"fc_flip_{i}", use_container_width=True):
                    fs = st.session_state["fc_flipped"]
                    fs.discard(i) if i in fs else fs.add(i)
                    st.rerun()

        b1, b2 = st.columns(2)
        with b1:
            if st.button("Reveal All", icon=":material/visibility:", key="fc_all",
                         use_container_width=True):
                st.session_state["fc_flipped"] = set(range(len(cards))); st.rerun()
        with b2:
            if st.button("Hide All", icon=":material/visibility_off:", key="fc_hide",
                         use_container_width=True):
                st.session_state["fc_flipped"] = set(); st.rerun()

# =============================================================================
# TAB 4 — CONCEPT EXPLAINER
# =============================================================================
with tab_explain:
    st.subheader(":material/lightbulb: Concept Explainer")
    st.caption("The same concept explained at 3 levels — from scratch to exam-ready.")
    ex_concept = st.text_input("Concept / Topic", placeholder="e.g. Deadlock in OS", key="ex_c")
    ex_level = st.radio("Level", ["beginner", "intermediate", "exam-ready"],
                        format_func=lambda x: {"beginner": "Beginner",
                                               "intermediate": "Intermediate",
                                               "exam-ready": "Exam-Ready"}[x],
                        horizontal=True, key="ex_l")
    if st.button("Explain", icon=":material/psychology:", type="primary",
                 use_container_width=True, key="ex_btn"):
        if not ex_concept.strip():
            st.error("Enter a concept.")
        else:
            try:
                with st.spinner(f"Explaining at **{ex_level}** level…"):
                    explanation = explain_concept(ex_concept.strip(), ex_level, user_id)
                st.markdown("<div class='td-card'>", unsafe_allow_html=True)
                st.markdown(explanation)
                st.markdown("</div>", unsafe_allow_html=True)
                st.download_button("Save explanation (.txt)", icon=":material/download:",
                    data=explanation.encode(),
                    file_name=f"explain_{ex_concept[:20].replace(' ', '_')}_{ex_level}.txt",
                    mime="text/plain", key="ex_dl")
            except MissingAPIKeyError as e:
                _key_error(e)

# =============================================================================
# TAB 5 — SUMMARY LEVELS
# =============================================================================
with tab_summary:
    st.subheader(":material/summarize: Summary Levels")
    st.caption("Get 1-sentence, 1-paragraph, or full structured summaries of any topic.")
    sm_topic = st.text_input("Topic", placeholder="e.g. Convolutional Neural Networks", key="sm_t")
    sm_len = st.radio("Length", ["sentence", "paragraph", "full"],
                      format_func=lambda x: {"sentence": "1 Sentence", "paragraph": "Paragraph",
                                             "full": "Full"}[x],
                      horizontal=True, key="sm_l")
    if st.button("Summarise", icon=":material/notes:", type="primary",
                 use_container_width=True, key="sm_btn"):
        if not sm_topic.strip():
            st.error("Enter a topic.")
        else:
            try:
                with st.spinner("Summarising…"):
                    summary = summarise_topic(sm_topic.strip(), sm_len, user_id)
                st.markdown("<div class='td-card'>", unsafe_allow_html=True)
                st.markdown(summary)
                st.markdown("</div>", unsafe_allow_html=True)
                st.download_button("Save (.txt)", icon=":material/download:",
                    data=summary.encode(),
                    file_name=f"summary_{sm_topic[:20].replace(' ', '_')}.txt",
                    mime="text/plain", key="sm_dl")
            except MissingAPIKeyError as e:
                _key_error(e)

# =============================================================================
# TAB 6 — DIAGRAM TO TEXT
# =============================================================================
with tab_diag:
    st.subheader(":material/image: Diagram-to-Text Explainer")
    st.caption("Upload a diagram, flowchart, circuit, or whiteboard photo — get a full text explanation.")
    diag_file = st.file_uploader("Upload diagram image",
        type=["png", "jpg", "jpeg", "webp", "bmp"], key="diag_up")
    if diag_file:
        col_img, col_res = st.columns(2)
        with col_img:
            st.image(diag_file, caption="Uploaded diagram", use_container_width=True)
        with col_res:
            if st.button("Explain This Diagram", icon=":material/search:", type="primary",
                         use_container_width=True, key="diag_btn"):
                try:
                    with st.spinner("Analysing diagram with vision model…"):
                        mime = f"image/{diag_file.name.rsplit('.', 1)[-1].lower()}"
                        if mime == "image/jpg":
                            mime = "image/jpeg"
                        explanation = explain_diagram_image(diag_file.getvalue(), mime, user_id)
                    st.markdown("<div class='td-card'>", unsafe_allow_html=True)
                    st.markdown(explanation)
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.download_button("Save explanation (.txt)", icon=":material/download:",
                        data=explanation.encode(),
                        file_name=f"diagram_explanation_{diag_file.name}.txt",
                        mime="text/plain", key="diag_dl")
                except MissingAPIKeyError as e:
                    _key_error(e)
                except Exception as ex:
                    st.error(f"Error: {ex}")

# =============================================================================
# TAB 7 — EXPORT (TXT only)
# =============================================================================
with tab_export:
    st.subheader(":material/ios_share: Export Conversation")
    st.caption("Download the current chat as a plain text file.")

    msgs = st.session_state.get("message_history", [])
    thread_title = get_thread_title(thread_key) or "Chat Export"

    if not msgs:
        st.info("No messages yet. Start a conversation in the **Chat** tab first.",
                icon=":material/info:")
    else:
        st.markdown(f"**Thread:** {thread_title} &nbsp;·&nbsp; **{len(msgs)} messages**")
        with st.expander("Preview", expanded=False):
            for m in msgs:
                st.markdown(f"{m['content'][:200]}{'…' if len(m['content']) > 200 else ''}")
                st.divider()

        safe = thread_title[:30].replace(" ", "_").replace("/", "-")
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        txt = export_conversation_txt(msgs, thread_title)
        st.download_button("Download .txt", icon=":material/download:", data=txt.encode(),
            file_name=f"{safe}_{date_str}.txt", mime="text/plain",
            use_container_width=True, type="primary", key="exp_txt_dl")
        st.text_area("Preview", value=txt[:2000] + ("…" if len(txt) > 2000 else ""),
                     height=250, key="exp_txt_preview", label_visibility="collapsed")
