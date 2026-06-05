from typing import TypedDict, List, Annotated
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage, SystemMessage,ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool
import requests
from langchain_groq import ChatGroq
import os
import sqlite3

load_dotenv()

# ✅ Sahi tarika
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)
search_tool = DuckDuckGoSearchRun(region="us-en")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
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
        
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}


@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=C9PE94QUEW9VWGFM"
    r = requests.get(url)
    return r.json()

tools = [get_stock_price, search_tool, calculator]

# Make the LLM tool-aware
llm_with_tools = llm.bind_tools(tools)

# ✅ State with add_messages
class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

# ✅ Node
def chat_node(state: ChatState):
    messages = state['messages']

    tool_result_ids = {
        m.tool_call_id
        for m in messages
        if isinstance(m, ToolMessage)
    }

    cleaned = []
    for msg in messages:
        if isinstance(msg, AIMessage) and msg.tool_calls:
            valid = [tc for tc in msg.tool_calls if tc['id'] in tool_result_ids]
            if len(valid) != len(msg.tool_calls):
                msg = AIMessage(content=msg.content or "")
        cleaned.append(msg)

    # ✅ Yahan replace karo purana system message
    system = SystemMessage(content="""You are a helpful assistant. 
You have access to tools for web search, stock prices, and calculations.
Only use tools when explicitly needed (e.g. stock prices, math, web search).
For normal conversation like greetings, just reply normally. Do NOT call any tools for casual chat.""")
    
    response = llm_with_tools.invoke([system] + cleaned)
    return {"messages": [response]}
tool_node = ToolNode(tools)

# ✅ SQLite
conn = sqlite3.connect("chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

# ✅ Graph
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools",tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge("tools","chat_node")

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)    
        