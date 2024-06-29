# LangChain sample application with RAG Agent

This is a simple LangChain Agent that will retrive the information from a PDF file and provide answers using the OpenAI llm.

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


## How does the program work

When you run the program with ` python main.py ` you will get a prompt

```
Prompt:
```

Enter your question into the Prompt as follows

```
Prompt: What is wealth management?
```

The prompt will Answer as follows -

```
Prompt: What is wealth management?

Wealth management involves professionals managing other people's money by investing funds across publicly traded stocks, bonds, managed funds, real estate, alternatives, and other opportunities based on readily available information. These professionals manage investments for specific purposes such as risk control, income, growth, or funding retirement, education, or a home purchase. The profession of wealth management began when it became possible to easily invest in multiple opportunities. Wealth management is an inherently uncertain activity, but the approach to managing wealth is becoming increasingly systematic with strategies like indexing, smart beta/factor investing, and pure alpha investing.

Prompt: 
```

To exit from the prompt enter exit or quit

```
Prompt:exit
```

or

```
Prompt:quit
```