# Create an agent with function calling and RAG pattern
# Reference: https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/#agents

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class AgentToolCall:
    def __init__(self, llm, tools):
        self.x_llm = llm
        self.x_tools = tools

    def setPrompt(self, prompt):
        self.x_prompt = prompt    
        
    def createAgent(self):
        agent = create_tool_calling_agent(self.x_llm, self.x_tools, self.x_prompt)
        return AgentExecutor(agent=agent, tools=self.x_tools, verbose=True)
