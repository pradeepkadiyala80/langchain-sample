from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

def get_model():
    llm = Ollama(model="llama2")
    return llm

def getEmbeddings():
    embeddings = OllamaEmbeddings()
    return embeddings
