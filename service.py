from pkjm.agents.agent import WealthManagementAgent
from langchain_core.messages import HumanMessage, AIMessage

WealthManagementAgent = WealthManagementAgent("./files/")

def chat_with_agent(query: str):    
    chat_history = []
    wm_agent_executor = WealthManagementAgent.agent_executor()
    human_msg = HumanMessage(content=query)
    chat_history.append(human_msg)
    response = wm_agent_executor.invoke({
        "input": query,
        "chat_history": chat_history
    })
    chat_history.append(AIMessage(content=response["output"]))
    return response["output"]
