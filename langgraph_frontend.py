from typing import TypedDict, List
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Load env variables
load_dotenv()

# LLM setup
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    huggingfacehub_api_token="HUGGINGFACE_API_KEY",   # ⚠️ apna token yahan daalo
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# ✅ State define
class ChatState(TypedDict):
    message: List[str]

# ✅ Node function (function hoga, class nahi)
def chat_node(state: ChatState):
    message = state["message"]
    response = model.invoke(message)
    return {"message": [response]}

# ✅ Memory
checkpointer = InMemorySaver()

# ✅ Graph build
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
