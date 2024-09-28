from fastapi import APIRouter
from entities.CustomAgent import CustomAgent
from typing import Any

from service import chat_with_agent, chat_custom_agent
router = APIRouter()

import json

@router.get("/status", tags=["wm_agent"])
async def wm():
    return [{"agent": "Hello the agent is active!"}]

@router.post("/agent", tags=["chat_agent"])
async def agent(query: str):
    answer = chat_with_agent(query)
    return {"query": query, "answer": answer}

@router.post("/agent/toocall")
async def custom_agent(agent: CustomAgent) -> Any:
    answer = chat_custom_agent(agent)
    return {"answer": answer}

@router.post("/agent/prompt")
async def custom_agent(agent: CustomAgent) -> Any:
    answer = chat_custom_agent(agent)
    return {"answer": answer}