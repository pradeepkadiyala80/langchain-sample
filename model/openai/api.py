from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

apiKey="sk-proj-1dAhe3eJdJdzTzW9fGi6T3BlbkFJ1WJ9qbHovw4rbdt23yDg"

def get_model():
    llm = ChatOpenAI(api_key=apiKey)
    return llm

def getEmbeddings():
    embeddings = OpenAIEmbeddings(openai_api_key=apiKey)
    return embeddings