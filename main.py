import sys

from pkjm.agents.agent_toolcall import AgentToolCall
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs
from pkjm.models.modelfactory import ModelFactory
from pkjm.prompts.prompt_factory import PromptFactory
from pkjm.prompts.example import ExampleSelectorFactory

from langchain_core.messages import HumanMessage, AIMessage

from langchain.globals import set_verbose

set_verbose(True)

from config import (
    MODEL_CONFIG, 
    DOCUMENTS, 
    RETRIEVER_TOOL_CONFIG, 
    PROMPT_CONFIG, 
    EXAMPLE_SELECTOR
)

# Need to work on this
chat_history = []

# Define Model to be used
model_type = MODEL_CONFIG.pop("model_type")
llm = ModelFactory.get_model(model_name=model_type, **MODEL_CONFIG)

# #Define the Retriver for RAG
retriever = LangChainRetriever()    
documents = load_docs(DOCUMENTS["file_path"])
retriever.build_vectorstore(documents)

# Instantiate example selector
example_select = ExampleSelectorFactory.build_selector(**EXAMPLE_SELECTOR)
example_prompt = PromptFactory.buildExamplePrompt()


while True:
    # Initialize the retriver with file documents
    retriever_tool = retriever.get_retriever_tool(
        RETRIEVER_TOOL_CONFIG["name"], 
        RETRIEVER_TOOL_CONFIG["description"]
    )   
    
    # Console Prompt to take the user input
    query = input('Prompt: ')    

    agent = AgentToolCall(llm, [retriever_tool])       

    # # Get the valid examples using input_variables
    fewshots_prompt = PromptFactory.buildFewShotsChatPrompt(example_select, 
                                                            example_prompt, 
                                                            PROMPT_CONFIG["prompt_input_varaibles"])
    
    system_message = PROMPT_CONFIG["system_message"] + "\n\n" + fewshots_prompt.format(input=query) 
    
    prompt_template = PromptFactory.buildChatPrompt(system_message)    
    agent.setPrompt(prompt_template)

    #To exit: use 'exit', 'quit', 'q', or Ctrl-D in the Prompt.",
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()
    #User Input is taken as a human message  
    human_msg = HumanMessage(content=query)
    # Maintain the chat history in memory
    chat_history.append(human_msg)    
    
    # Invoke the agent executor with a input query
    agent_executor = agent.createAgent()   

    
    response = agent_executor.invoke({
        "input": query
    })
    # Append the responses from AI as aAI messages
    chat_history.append(AIMessage(content=response["output"]))
    # Print the Output
    print(response["output"])
    