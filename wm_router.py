from fastapi import APIRouter

from wm_service import chat_with_agent
router = APIRouter()

@router.get("/wm/", tags=["wm_agent"])
async def wm():
    return [{"agent": "Hello!"}]

@router.post("/wm/agent", tags=["chat_agent"])
async def wm_agent(query: str):
    answer = chat_with_agent(query)
    return {"query": query, "answer": answer}
