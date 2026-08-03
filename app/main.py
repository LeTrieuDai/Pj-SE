from fastapi import FastAPI
from app.database import client
from app.routers.tasks import router as task_router

app = FastAPI(
    title="Pj-SE Todo API",
    version="1.0.0"
)

app.include_router(task_router)

@app.get("/")
async def root():
    return {
        "message": "Hello Todo API",
        "status": "MongoDB Connected"
    }
    