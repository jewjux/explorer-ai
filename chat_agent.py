from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()
agents = {}
checkpointer = None


def get_checkpoint(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    global checkpointer
    if checkpointer is None:
        checkpointer = SqliteSaver.from_conn_string("data/curiosity.db")
    return checkpointer.get(config)


def get_agent(model_id: str):
    global agents
    if not model_id in agents:
        search = TavilySearchResults(max_results=5, include_images=True)
        tools = [search]
        global checkpointer
        cp = SqliteSaver.from_conn_string("data/curiosity.db")
        if model_id == "meta/llama-3.1-405b-instruct":
            model = ChatNVIDIA(model=model_id, api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        elif model_id == "meta/llama-3.2-3b-instruct":
            model = ChatNVIDIA(model=model_id, api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        elif model_id == "meta/llama3-8b-instruct":
            model = ChatNVIDIA(model=model_id, api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        elif model_id == "microsoft/phi-3-medium-4k-instruct":
            model = ChatNVIDIA(model=model_id, api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        else:
            raise Exception(f"Model not supported: {model_id}")
        agent = create_react_agent(model, tools, checkpointer=cp)
        agents[model_id] = agent
    return agents[model_id]
