from fastapi import FastAPI

import wm_router

app = FastAPI()
app.include_router(wm_router.router)
