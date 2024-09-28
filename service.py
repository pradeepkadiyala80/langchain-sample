from pkjm.agents.agent_toolcall import AgentToolCall
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs
from pkjm.models.modelfactory import ModelFactory
from entities.CustomAgent import CustomAgent

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

from config import MODEL_CONFIG, DOCUMENTS, RETRIEVER_TOOL_CONFIG, PROMPT_CONFIG

import json

model_type = MODEL_CONFIG.pop("model_type")
llm = ModelFactory.get_model(model_name=model_type, **MODEL_CONFIG)

retriever = LangChainRetriever()    
documents = load_docs(DOCUMENTS["file_path"])
retriever.build_vectorstore(documents)
retriever_tool = retriever.get_retriever_tool(
        RETRIEVER_TOOL_CONFIG["name"], 
        RETRIEVER_TOOL_CONFIG["description"]
        )

def chat_with_agent(query: str):
    chat_history = []    
    agentX = AgentToolCall(llm, [retriever_tool])    
    human_msg = HumanMessage(content=query)
    chat_history.append(human_msg)
    agentX.createPrompt(PROMPT_CONFIG["system_message"])    
    return call_agent(agentX)

def chat_custom_agent(custom_agent: CustomAgent) -> any:
    chat_history = []  
    agentX = AgentToolCall(llm, [retriever_tool])        
    prompt_message = custom_agent.prompt_template
    human_msg = HumanMessage(content=custom_agent.query)
    chat_history.append(human_msg)
    agentX.createPrompt(prompt_message)    
    return call_agent(agentX, chat_history=chat_history)

def call_agent(agentX: AgentToolCall, chat_history: list):
    agentX.createPrompt(PROMPT_CONFIG["system_message"])
    response = agentX.createAgent().invoke({
        "messages": chat_history        
    })
    chat_history.append(AIMessage(content=response["output"]))
    return response["output"]
