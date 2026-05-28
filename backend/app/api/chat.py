from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.workflow import workflow

router = APIRouter()


class ChatRequest(BaseModel):
    query: str


@router.post("/chat")
def chat(request: ChatRequest):

    result = workflow.invoke({
        "query": request.query
    })

    return {
        "response": result["report"]
    }
