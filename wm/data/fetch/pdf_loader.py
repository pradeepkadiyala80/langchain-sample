from langchain_community.document_loaders import PyPDFLoader

def load_pdfdoc(filepath):
    loader = PyPDFLoader(filepath)
    return loader.load()
