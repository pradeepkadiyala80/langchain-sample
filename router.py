from fastapi import APIRouter
from typing import Any
from entities.Chat import Chat

#from service import chat_with_agent, chat_custom_agent
from service import chat_with_fewshots
router = APIRouter()

@router.get("/status", tags=["wm_agent"])
async def wm():
    return [{"agent": "Hello the agent is active!"}]

@router.post("/agent/fewshots", tags=["fewshots"])
async def agent_fewshots(chat: Chat):
    print(chat)
    answer = chat_with_fewshots(chat.message)
    print({"query": chat.message, "answer": answer})
    return {"query": chat.message, "answer": answer}
