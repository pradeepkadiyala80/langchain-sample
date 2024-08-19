# Wealth Management Retriever tool which uses the docloader
# Reference: https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/

from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool

from langchain_community.vectorstores import FAISS

from pkjm.tools.doc_loader import load_docs

import os

# class RetrieverTool:
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         self.text_splitter = CharacterTextSplitter(
#             separator = "\n",
#             chunk_size = 1000,
#             chunk_overlap  = 200, #striding over the text
#             length_function = len,
#         )


#     def create_retriever(self):        
#         embeddings = embeddings = OpenAIEmbeddings()
#         documents = load_docs(self.folder_path)
#         splits = self.text_splitter.split_documents(documents)        
#         vector_store = FAISS.from_documents(documents=splits, embedding=embeddings)
#         return vector_store.as_retriever()
    
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.tools import tool

class LangChainRetriever:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        # Initialize the embeddings model
        self.text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 200, #striding over the text
            length_function = len,
        )
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
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

# Example usage
# if __name__ == "__main__":
#     documents = [
#         "This is a document about machine learning.",
#         "This is a document about deep learning.",
#         "This document covers transformers.",
#         "Natural language processing is fascinating.",
#         "We are learning about embeddings."
#     ]

#     # Initialize the retriever with a chosen model
#     retriever = LangChainRetriever(model_name="all-MiniLM-L6-v2")
    
#     # Build the vectorstore with documents
#     retriever.build_vectorstore(documents)

#     # Retrieve the top 3 similar documents to the query
#     query = "Tell me something about NLP."
#     results = retriever.retrieve(query, top_k=3)

#     print("Query:", query)
#     print("\nTop 3 similar documents:")
#     for doc in results:
#         print(f"Document: {doc.page_content}")



