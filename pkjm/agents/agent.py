from pkjm.agents.agent_toolcall import AgentToolCall
from pkjm.tools.retriever import LangChainRetriever
from pkjm.tools.doc_loader import load_docs
from pkjm.models.modelfactory import ModelFactory
from pkjm.prompts.prompt_factory import PromptFactory
from pkjm.prompts.example import ExampleSelectorFactory

from langchain_core.messages import HumanMessage, AIMessage

from langchain.globals import set_verbose

from config import (
    MODEL_CONFIG, 
    DOCUMENTS, 
    RETRIEVER_TOOL_CONFIG, 
    PROMPT_CONFIG, 
    EXAMPLE_SELECTOR
)

class AgentFactory:
    
    @staticmethod
    def get_agent_fewshots_chat_prompt(query: str):    
        # Need to work on this
        chat_history = []    

        # Instantiate example selector
        example_select = ExampleSelectorFactory.build_selector(**EXAMPLE_SELECTOR)
        example_prompt = PromptFactory.buildExamplePrompt()

        ## MODEL_CONFIG has args like model_type 
        ## Copy MODEL_CONFIG because when you pop moddel_type the consecutive requests will not loose it 
        kwargs_copy = dict(MODEL_CONFIG)
        print(kwargs_copy)
        model_type = kwargs_copy.pop("model_type")
        llm = ModelFactory.get_model(model_name=model_type, **kwargs_copy)

        # #Define the Retriver for RAG
        retriever = LangChainRetriever()    
        documents = load_docs(DOCUMENTS["file_path"])
        retriever.build_vectorstore(documents)

        # Initialize the retriver with file documents
        retriever_tool = retriever.get_retriever_tool(
            RETRIEVER_TOOL_CONFIG["name"], 
            RETRIEVER_TOOL_CONFIG["description"]
        )

        agent = AgentToolCall(llm, [retriever_tool])
        
        # Get the valid examples using input_variables
        fewshots_prompt = PromptFactory.buildFewShotsChatPrompt(example_select, 
                                                                example_prompt, 
                                                                PROMPT_CONFIG["prompt_input_varaibles"])
        system_message = PROMPT_CONFIG["system_message"] + "\n\n" + fewshots_prompt.format(input=query) 

        # Get Prompt Template
        prompt_template = PromptFactory.buildChatPrompt(system_message)    
        agent.setPrompt(prompt_template)
        agent_executor = agent.createAgent() 

        return agent_executor