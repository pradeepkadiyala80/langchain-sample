from typing import Any, Dict, Type
from langchain.llms import BaseLLM
from langchain_openai import ChatOpenAI
from langchain_mistralai.chat_models import ChatMistralAI

class ModelFactory:
    MODEL_MAPPING = {
        "chatopenai": ChatOpenAI,
        "mistralai": ChatMistralAI
    }

    @staticmethod
    def get_model(model_name: str, **kwargs) -> BaseLLM:
        """
        Static method to get an LLM instance based on the model name.

        :param model_name: The name of the model (e.g., 'openai', 'cohere', etc.)
        :param kwargs: The parameters required to initialize the model.
        :return: An instance of the specified LLM.
        """
        model_class = ModelFactory.MODEL_MAPPING.get(model_name.lower())
        if model_class is None:
            raise ValueError(f"Model {model_name} is not supported. Available models: {list(ModelFactory.MODEL_MAPPING.keys())}")
        
        return model_class(**kwargs)


    