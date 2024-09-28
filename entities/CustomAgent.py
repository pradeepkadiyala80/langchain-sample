from pydantic import BaseModel

class CustomAgent(BaseModel):
    prompt_template: str
    query: str