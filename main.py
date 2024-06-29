import os
import sys

from wm.agents.wm_agent import WealthManagementAgent
from langchain_core.messages import HumanMessage, AIMessage

WealthManagementAgent = WealthManagementAgent("./files/")
chat_history = []

wm_agent_executor = WealthManagementAgent.agent_executor()

while True:
    query = input('Prompt: ')
    #To exit: use 'exit', 'quit', 'q', or Ctrl-D.",
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()
    human_msg = HumanMessage(content=query)
    chat_history.append(human_msg)
    response = wm_agent_executor.invoke({
        "input": query,
        "chat_history": chat_history
    })
    chat_history.append(AIMessage(content=response["output"]))
    print(response["output"])

    