from pkjm.agents.agent import AgentX
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

import os
apiKey = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=apiKey,temperature=0, model="gpt-3.5-turbo")
retriever = LangChainRetriever()    
documents = load_docs("./files/")
retriever.build_vectorstore(documents)
retriever_tool = retriever.get_retriever_tool(
        "WealthManagementRetrievalTool", 
        "Find the contenet from the wealth management document and provide response with in the context"
        )
agentX = AgentX(llm, [retriever_tool])
agentX.createPrompt("You are a helpful Wealth Management assistant.")

def chat_with_agent(query: str):    
    chat_history = []    
    human_msg = HumanMessage(content=query)
    chat_history.append(human_msg)
    response = agentX.createAgent().invoke({
        "messages": chat_history        
    })
    chat_history.append(AIMessage(content=response["output"]))
    return response["output"]
