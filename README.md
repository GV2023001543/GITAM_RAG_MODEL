# 🤖 RAG Chatbot - LangGraph

A Multi-Utility AI Chatbot built with LangGraph, FAISS, and Groq LLM.

## ✨ Features
- 📄 PDF Upload & Question Answering (RAG)
- 🔍 Web Search (Tavily)
- 📈 Stock Price Lookup (Yahoo Finance)
- 🧮 Calculator
- 💬 Multi-turn Conversation Memory

## 🛠️ Tech Stack
- **LangGraph** - AI workflow orchestration
- **FAISS** - Vector similarity search
- **HuggingFace Embeddings** - all-MiniLM-L6-v2
- **Groq LLM** - llama-3.3-70b-versatile
- **Streamlit** - Frontend UI

## 🚀 Live Demo
[Click here to try!](https://anamika-rag-chatbot.streamlit.app/)

## ⚙️ Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add API keys in `.env`:
   - GROQ_API_KEY
   - TAVILY_API_KEY
4. Run: `streamlit run langgraph_rag_frontend.py`
