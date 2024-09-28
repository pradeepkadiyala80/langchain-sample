# Reference https://python.langchain.com/v0.1/docs/modules/model_io/prompts/example_selectors/

from langchain_core.example_selectors.base import BaseExampleSelector
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from langchain_community.example_selectors.ngram_overlap import (
    NGramOverlapExampleSelector,
)

from langchain_core.example_selectors import (
    MaxMarginalRelevanceExampleSelector,
    SemanticSimilarityExampleSelector
)

class ExampleSelector(BaseExampleSelector):    
    def __init__(self, examples, num, prompt, threashold):
        self.examples = examples
        self.num = num
        self.prompt = prompt
        self.threashold = threashold

    def add_example(self, example):
        self.examples.append(example)


class ExampleSelectorFactory:
    SelectorMap = {
        "mmr": MaxMarginalRelevanceExampleSelector,
        "n-gram": NGramOverlapExampleSelector,
        "similarity": SemanticSimilarityExampleSelector
    }

    @staticmethod
    def build_selector(**kwargs):
        type = kwargs.pop("type")
        selector_class =  ExampleSelectorFactory.SelectorMap.get(type.lower())

        if selector_class is None:
            raise ValueError(f"Example Selector {selector_class} is not supported. Available templates: {list(ExampleSelectorFactory.SelectorMap.keys())}")

        if type == "mmr":
            return ExampleSelectorFactory.buid_maxmarginal_reference_selector(**kwargs)
        elif type == "n-gram":
            return ExampleSelectorFactory.build_ngram_selector(**kwargs)
        elif type == "similarity":
            return ExampleSelectorFactory.build_semantic_selector(**kwargs)
        else:
            return None

    
    @staticmethod
    def build_semantic_selector(**kwargs):
        examples = kwargs.pop("examples")
        k = kwargs.pop("num")

        if examples is None:
            raise ValueError(f"examples in kwargs of the selector {kwargs} is not valid.")
        
        if k is None:
            k = 3
        
        return SemanticSimilarityExampleSelector.from_examples(
            examples,
            OpenAIEmbeddings(),
            FAISS,
            k=k
        )
    
    @staticmethod
    def buid_maxmarginal_reference_selector(**kwargs):
        examples = kwargs.pop("examples")
        k = kwargs.pop("num")

        if examples is None:
            raise ValueError(f"examples in kwargs of the selector {kwargs} is not valid.")
        
        if k is None:
            k = 3
        
        #selector = ExampleSelector(examples=examples, num=k)
        return MaxMarginalRelevanceExampleSelector.from_examples(
                examples,
                OpenAIEmbeddings(),
                FAISS,
                k
            )    
            
    
    @staticmethod    
    def build_ngram_selector(**kwargs):
        examples = kwargs.pop("examples")
        prompt = kwargs.pop("prompt")
        threashhold = kwargs.pop("threshold")

        if examples is None:
            raise ValueError(f"examples in kwargs of the selector {kwargs} is not valid.")
        
        if prompt is None:
            raise ValueError(f"prompt in kwargs of the selector {kwargs} is not valid.")
        
        if threashhold is None:
            raise ValueError(f"threashhold in kwargs of the selector {kwargs} is not valid.")

        ex_selector = ExampleSelector(examples=examples, prompt=prompt, threashold=threashhold)
        return NGramOverlapExampleSelector(            
            examples=ex_selector.examples,
            example_prompt=ex_selector.prompt,
            threshold=ex_selector.threashold,
        )
    