import os
import sys

from langchain_openai import ChatOpenAI

from pkjm.agents.agent import AgentX
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs
from pkjm.models.modelfactory import ModelFactory

from langchain_core.messages import HumanMessage, AIMessage

from config import MODEL_CONFIG, DOCUMENTS, RETRIEVER_TOOL_CONFIG, PROMPT_CONFIG

chat_history = []

model_type = MODEL_CONFIG.pop("model_type")
llm = ModelFactory.get_model(model_name=model_type, **MODEL_CONFIG)

retriever = LangChainRetriever()    
documents = load_docs(DOCUMENTS["file_path"])
retriever.build_vectorstore(documents)

while True:
    # Initialize the retriver with file documents
    retriever_tool = retriever.get_retriever_tool(
        RETRIEVER_TOOL_CONFIG["name"], 
        RETRIEVER_TOOL_CONFIG["description"]
        )   
    
    # Console Prompt to take the user input
    query = input('Prompt: ')
    agentX = AgentX(llm, [retriever_tool])
    agentX.createPrompt(PROMPT_CONFIG["system_message"])

    #To exit: use 'exit', 'quit', 'q', or Ctrl-D in the Prompt.",
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()
    # User Input is taken as a human message  
    human_msg = HumanMessage(content=query)
    # Maintain the chat history in memory
    chat_history.append(human_msg)    
    # Invoke the agent executor with a input query
    response = agentX.createAgent().invoke({
        "messages": chat_history        
    })    
    # Append the responses from AI as aAI messages
    chat_history.append(AIMessage(content=response["output"]))
    # Print the Output
    print(response["output"])
