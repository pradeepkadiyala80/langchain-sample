from langchain_core.prompts import ChatPromptTemplate

wm_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful Wealth Management assistant.",
        ),
        ("placeholder", "{chat_history}"),
        ("placeholder", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
        ("placeholder", "{messages}"),
        
    ]
)
