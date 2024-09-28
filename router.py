from fastapi import APIRouter
from typing import Any

#from service import chat_with_agent, chat_custom_agent
from service import chat_with_fewshots
router = APIRouter()

@router.get("/status", tags=["wm_agent"])
async def wm():
    return [{"agent": "Hello the agent is active!"}]

@router.post("/agent/fewshots", tags=["fewshots"])
async def agent_fewshots(query: str):
    answer = chat_with_fewshots(query)
    return {"query": query, "answer": answer}
