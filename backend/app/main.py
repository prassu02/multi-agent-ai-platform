from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.api.health import router as health_router

app = FastAPI(title="Multi-Agent AI Platform")

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": "AI Platform Running"
    }
