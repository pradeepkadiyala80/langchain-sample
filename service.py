from pkjm.agents.agent import AgentX
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs
from pkjm.models.modelfactory import ModelFactory

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

from config import MODEL_CONFIG, DOCUMENTS, RETRIEVER_TOOL_CONFIG, PROMPT_CONFIG

model_type = MODEL_CONFIG.pop("model_type")
llm = ModelFactory.get_model(model_name=model_type, **MODEL_CONFIG)

retriever = LangChainRetriever()    
documents = load_docs(DOCUMENTS["file_path"])
retriever.build_vectorstore(documents)
retriever_tool = retriever.get_retriever_tool(
        RETRIEVER_TOOL_CONFIG["name"], 
        RETRIEVER_TOOL_CONFIG["description"]
        )
agentX = AgentX(llm, [retriever_tool])
agentX.createPrompt(PROMPT_CONFIG["system_message"])

def chat_with_agent(query: str):    
    chat_history = []    
    human_msg = HumanMessage(content=query)
    chat_history.append(human_msg)
    response = agentX.createAgent().invoke({
        "messages": chat_history        
    })
    chat_history.append(AIMessage(content=response["output"]))
    return response["output"]
