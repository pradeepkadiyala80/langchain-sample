from pkjm.agents.agent import AgentFactory


def chat_with_fewshots(query: str):
    agent = AgentFactory.get_agent_fewshots_chat_prompt(query)
    output = agent.invoke({
        "input": query
    })
    return output
