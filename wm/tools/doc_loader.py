# Wealth Management Document Loader Tool Definition
# Reference: https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/

import os

from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document


def load_docs(folder_path):        
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file = os.path.join(folder_path, filename)
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            document = Document(page_content=text, metadata={"document_name": filename})
            documents.append(document)
    return documents