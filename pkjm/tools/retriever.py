# Wealth Management Retriever tool which uses the docloader
# Reference: https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/

from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool

from langchain_community.vectorstores import FAISS    
from langchain.tools import tool

class LangChainRetriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        # Initialize the embeddings model
        self.text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 200, #striding over the text
            length_function = len,
        )        
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None

    def build_vectorstore(self, documents: list):
        # Create FAISS vectorstore from documents
        splits = self.text_splitter.split_documents(documents)
        self.vectorstore = FAISS.from_documents(documents=splits, embedding=self.embeddings)
    
    def get_retriever(self):
        return self.vectorstore.as_retriever(search_kwargs={"k": 5})

    def get_retriever_tool(self, name, description):
        print("Building Retriever \n")
        print(self.get_retriever())
        return create_retriever_tool(
            self.get_retriever(),
            name,
            description
        )

    def retrieve(self, query: str, top_k: int = 5):
        """Retrive the text from documents"""
        retriever = self.vectorstore.as_retriever(search_kwargs={"k": top_k})
        return retriever.get_relevant_documents(query)



