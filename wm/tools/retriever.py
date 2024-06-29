# Wealth Management Retriever tool which uses the docloader
# Reference: https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/

from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS

from langchain_community.vectorstores import FAISS

from wm.tools.doc_loader import load_docs

import os

class RetrieverTool:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 200, #striding over the text
            length_function = len,
        )


    def create_retriever(self):        
        embeddings = embeddings = OpenAIEmbeddings()
        documents = load_docs(self.folder_path)
        splits = self.text_splitter.split_documents(documents)        
        vector_store = FAISS.from_documents(documents=splits, embedding=embeddings)
        return vector_store.as_retriever()
    



