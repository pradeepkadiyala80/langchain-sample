import os

api_key = os.environ.get("OPENAI_API_KEY")

SERVER = {
    "route_prefix": "/pkjm"
}

MODEL_CONFIG = {
    "model_type": "chatopenai",
    "name": "gpt-4o",
    "temperature": 0,
    "api_key": api_key
}

DOCUMENTS = {
    "file_path": "./files/"
}

RETRIEVER_TOOL_CONFIG = {
    "name": "DocumentRetriever",
    "description": "A tool that will take the list of pdf documents and retreives content based on the query using vector store",
}

EXAMPLES = [    
    {
        "input": "How is Bond and CD pricing different from stock pricing?",
        "output": "Bond and CD pricing is more complex than stock pricing due to the way they are traded, often using derived prices rather than last-trade prices. These prices factor in coupon rates, maturity, credit rating, and large trading blocks, but may not reflect the actual price in a sale. Despite this, bonds and CDs held to maturity will pay out at their full face value unless the issuer defaults."
    },
    {
        "input": "What is the performance review of FXAIX?",
        "output": "The fund matched the S&P 500 indexs 4.28 gain in Q2, benefiting from efficient trading and index replication. U.S. stocks performed well, driven by resilient corporate profits, AI excitement, and expectations of interest rate cuts. Growth stocks, especially in the tech and communication services sectors, led the rally, with AI-focused firms like Nvidia and Broadcom showing significant gains. The fund maintains a disciplined investment approach, focusing on minimizing tracking difference and error to align closely with benchmark performance."
    },
    {
        "input": "What is the outlook of the Stockmarket in July?",
        "output": "The US stock market has become even more concentrated than it had been in the early 2000s technology stock bubble, as a small number of stocks have driven most of the gains for the broadly based S&P 500 index. While the market has become historically top-heavy over the past 7 years—and increasingly so—stock valuations have not reached the excessive levels of the past. Moreover, rising performance dispersion among the largest components in the S&P 500 may be an opportunity, as it helps create room for active managers to add value through security selection. "
    },
    {
        "input": "What is compound interest?",
        "output": "Compound interest is when interest you earn in a savings or investment account earns interest of its own. (So meta.) In other words, you earn interest on both your initial balance—called the principal—and the interest thats added to the balance over time."
    },
    {
        "input": "How is the technology sector in 2024?",
        "output": "The technology sector has had an outstanding past year. A shifting macroeconomic environment in 2023 helped bring tech stocks back into favor with investors. The resulting rally was further fueled by groundbreaking advancements in artificial intelligence (AI), which heralded the possibility of a promising new era of innovation for the sector. "
    }
]

EXAMPLE_SELECTOR = {
    "type": "similarity",
    "examples": EXAMPLES,
    "num": 3
}

# PROMPT_CONFIG = {
#     "type": "chat_prompt_template",
#     "system_message": """You are a Financial Advisor on stocks. 
#     You should only provide information retrived from the pdf documents using the retriever tool
#     If the information retrieved is not related to the query then do not provide any information.
#     """
# }

PROMPT_CONFIG = {
    "type": "few_shots_prompt", 
    "example_template": """input: {input}
                            output: {output}
    """,
    "example_input_varibales": ["input", "output"],
    "prompt_input_varaibles": ["input"],
    "system_message": """You are a Financial Advisor on stocks. 
    You should only provide information retrived from the pdf documents using the retriever tool
    If the information retrieved is not related to the query then do not provide any information.
    Use the examples if provided to derive your answers.

    """
}
