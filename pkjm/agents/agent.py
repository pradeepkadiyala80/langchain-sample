# Create an agent with function calling and RAG pattern
# Reference: https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/#agents

from langchain.agents import create_openai_tools_agent, AgentExecutor, create_tool_calling_agent
from langchain.tools.retriever import create_retriever_tool

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# from pkjm.tools.retriever import RetrieverTool
# from pkjm.agents.prompts import wm_prompt

import os
apiKey = os.environ.get("OPENAI_API_KEY")

## Agent rquires llm, tools, prompt

# class WealthManagementAgent:
#     def __init__(self, filepath):
#         self.file_path = filepath

#     def agent_executor(self):  
#         # Use Open AI retreiver tool to fetch the document from file path and create embeddings
#         retriever_tool = RetrieverTool(folder_path=self.file_path)  
#         retriever = retriever_tool.create_retriever()
        
#         # Create a RAG using the retriever tool
#         wm_rag = create_retriever_tool(
#             retriever,
#             "WealthManagementRetrievalTool",
#             "Find the contenet from the wealth management document and provide response with in the context"
#         )

#         # Specify the Open AI model 
#         llm = ChatOpenAI(api_key=apiKey,temperature=0, model="gpt-3.5-turbo")
        
#         # Use the RAG retriver as a tool
#         tools = [wm_rag]        

#         # Create an agent as a tool calling agent with the prompt defined
#         agent = create_tool_calling_agent(llm, tools, wm_prompt)
#         return AgentExecutor(agent=agent, tools=tools)

class AgentX:
    def __init__(self, llm, tools):
        self.x_llm = llm
        self.x_tools = tools

    def setPrompt(self, prompt):
        self.x_prompt = prompt

    def createPrompt(self, ptSystemMessage):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "{system_message}"
                ),
                MessagesPlaceholder(variable_name="messages"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),                                
            ]
        )
        prompt = prompt.partial(system_message=ptSystemMessage)
        #prompt = prompt.partial(tool_names=", ".join([tool.name for tool in self.x_tools]))
        self.x_prompt = prompt
        
    def createAgent(self):
        agent = create_tool_calling_agent(self.x_llm, self.x_tools, self.x_prompt)
        return AgentExecutor(agent=agent, tools=self.x_tools)
