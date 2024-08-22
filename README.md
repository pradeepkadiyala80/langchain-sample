# LangChain sample application with RAG Agent

This is a simple LangChain Agent that will retrive the information from a PDF file and provide answers using the OpenAI llm.

## How to run it?

### 1. Install the python pacakages

```
python -m pip install -r requirements.txt
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

## How does the program work as an API


1. Install the following packages

```
python -m pip install fastapi
python -m pip install uvicorn
```
2. Run the server

`fastapi dev server.py`

## How to run in local dockerhub on Mac

### Pre-reqs

Install docker in your local machine

### Steps to create docker image and run

1. Create a Dockerfile from the sample provided

`cp Dockerfile.sample Dockerfile`

2. Update the OPENAI_API_KEY environment variable inside Dockerfile

`ENV OPENAI_API_KEY=<secret-openai_api-key>`

3. Build the docker image

`docker build -t ai-agent-fastapi .`

Note: This will take a lot of time to create the docker image

4. Run the image in a container

`docker run -d -p 8000:8000 ai-agent-fastapi`

5. Test the application

Open the browser and enter the url http://localhost:8000/docs

