from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts.few_shot import FewShotChatMessagePromptTemplate, PromptTemplate        

class PromptFactory:
    TemplateMapping = {
        "chat_prompt_template": ChatPromptTemplate,
        "few_shots_prompt": FewShotChatMessagePromptTemplate
    }

    @staticmethod
    def getPrompt(template: str, **kwargs):
        """
        Static method to get an ChatPromptTemplate instance based on the template name.

        :param template: The name of the template (e.g., 'chat_prompt_template')
        :param **kwargs: Prompt arguments.
        :return: An instance of the prompt.
        """
        template = template.lower()
        prompt_template_class = PromptFactory.TemplateMapping.get(template)
        if prompt_template_class is None:
            raise ValueError(f"Prompt Template {prompt_template_class} is not supported. Available templates: {list(PromptFactory.TemplateMapping.keys())}")
        
        if template == "chat_prompt_template":                             
            prompt = PromptFactory.buildChatPrompt(**kwargs)
            return prompt
        else:
            return None
        # elif template == "few_shots_prompt":
        #     prompt = PromptFactory.buildFewShotsPrompt(**kwargs)

    @staticmethod
    def buildChatPrompt(system_message):         
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "{system_message}"
                ),
                #MessagesPlaceholder(variable_name="messages"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),                                
            ]
        )
        prompt = prompt.partial(system_message=system_message)
        return prompt

    @staticmethod
    def buildChatPromptFromMessages(system_message, prompt):
        prompt = ChatPromptTemplate.from_messages(
            [
                prompt,
                ("system", "{system_message}"),                
                ("human", "{input}"),
                #MessagesPlaceholder(variable_name="messages"),
                MessagesPlaceholder(variable_name="agent_scratchpad")
            ]

        )
        prompt = prompt.partial(system_message=system_message)
        return prompt

    @staticmethod
    def buildFewShotsChatPrompt(selector, example_prompt, input_variables):
        return FewShotChatMessagePromptTemplate(
            example_selector=selector,
            example_prompt=example_prompt,            
            input_variables=input_variables
        )
    
    #def buildExamplePrompt(input_variables:list, template: str):
    @staticmethod
    def buildExamplePrompt():
        return ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"), 
                ("ai", "{output}")        
            ]
        )
