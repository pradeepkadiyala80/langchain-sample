import os
import sys

from wm.agents.wm_agent import WealthManagementAgent
from langchain_core.messages import HumanMessage, AIMessage

# Instansiate a wealthmanagement agent
WealthManagementAgent = WealthManagementAgent("./files/")
chat_history = []

while True:
    # Create agent executor
    wm_agent_executor = WealthManagementAgent.agent_executor()
    # Console Prompt to take the user input
    query = input('Prompt: ')
    #To exit: use 'exit', 'quit', 'q', or Ctrl-D in the Prompt.",
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()
    # User Input is taken as a human message    
    human_msg = HumanMessage(content=query)
    # Maintain the chat history in memory
    chat_history.append(human_msg)
    # Invoke the agent executor with a input query
    response = wm_agent_executor.invoke({
        "input": query,
        "chat_history": chat_history
    })
    # Append the responses from AI as aAI messages
    chat_history.append(AIMessage(content=response["output"]))
    # Print the Output
    print(response["output"])
