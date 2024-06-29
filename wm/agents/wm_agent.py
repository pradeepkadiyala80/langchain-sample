# Create an agent with function calling and RAG pattern
# Reference: https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/#agents

from langchain.agents import create_openai_tools_agent, AgentExecutor, create_tool_calling_agent
from langchain.tools.retriever import create_retriever_tool

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools

from wm.tools.retriever import RetrieverTool
from wm.agents.prompts import wm_prompt

apiKey="sk-proj-1dAhe3eJdJdzTzW9fGi6T3BlbkFJ1WJ9qbHovw4rbdt23yDg"

class WealthManagementAgent:
    def __init__(self, filepath):
        self.file_path = filepath

    def agent_executor(self):        
        retriever_tool = RetrieverTool(folder_path=self.file_path)  
        retriever = retriever_tool.create_retriever()

        wm_rag = create_retriever_tool(
            retriever,
            "WealthManagementRetrievalTool",
            "Find the contenet from the wealth management document and provide response with in the context"
        )

        llm = ChatOpenAI(api_key=apiKey,temperature=0, model="gpt-3.5-turbo")
        
        tools = [wm_rag]        

        agent = create_tool_calling_agent(llm, tools, wm_prompt)
        return AgentExecutor(agent=agent, tools=tools)