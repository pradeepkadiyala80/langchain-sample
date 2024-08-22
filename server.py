from fastapi import FastAPI

from config import SERVER
import router

app = FastAPI()
app.include_router(router.router, prefix=SERVER["route_prefix"])
