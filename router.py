from fastapi import APIRouter

from service import chat_with_agent
router = APIRouter()

@router.get("/status", tags=["wm_agent"])
async def wm():
    return [{"agent": "Hello the agent is active!"}]

@router.post("/agent", tags=["chat_agent"])
async def agent(query: str):
    answer = chat_with_agent(query)
    return {"query": query, "answer": answer}
