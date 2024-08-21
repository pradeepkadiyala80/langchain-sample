import os

api_key = os.environ.get("OPENAI_API_KEY")

MODEL_CONFIG = {
    "model_type": "chatopenai",
    "name": "gpt-3.5-turbo",    
    "temperature": 0,
    "api_key": api_key
}

DOCUMENTS = {
    "file_path": "./files/"
}

RETRIEVER_TOOL_CONFIG = {
    "name": "WealthManagementRetrievalTool",
    "description": "Find the contenet from the wealth management document and provide response with in the context",    
}

PROMPT_CONFIG = {
    "system_message": "You are a helpful Wealth Management assistant."
}