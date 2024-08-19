import os
import sys

from langchain_openai import ChatOpenAI

from pkjm.agents.agent import AgentX
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs

from langchain_core.messages import HumanMessage, AIMessage

apiKey = os.environ.get("OPENAI_API_KEY")

chat_history = []

llm = ChatOpenAI(api_key=apiKey,temperature=0, model="gpt-3.5-turbo")

retriever = LangChainRetriever()    
documents = load_docs("./files/")
retriever.build_vectorstore(documents)

while True:
    # Initialize the retriver with file documents
    retriever_tool = retriever.get_retriever_tool(
        "WealthManagementRetrievalTool", 
        "Find the contenet from the wealth management document and provide response with in the context"
        )   
    
    # Console Prompt to take the user input
    query = input('Prompt: ')
    agentX = AgentX(llm, [retriever_tool])
    agentX.createPrompt("You are a helpful Wealth Management assistant.")

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
