# LangChain sample application with RAG Agent

This is a simple LangChain Agent that will retrive the information from a PDF file and provide answers using the OpenAIChat llm.

## How to run it?

### 1. Install the python pcakages

```
pip install langchain
pip install langchain-core
pip install langchain-openai
pip install langchain-community
pip install langchain-text-splitters
pip install -U langchain-chroma
pip install pypdf
```

### 2. Get OpenAI Key and add the environment variable OPENAI_API_KEY

` export OPENAI_API_KEY="<Get the API Key from Open API account>" `

### 3. Run the program

` python main.py`

or

` python3 main.py`

