from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.workflow import app_graph

router = APIRouter()

class AgentRequest(BaseModel):
    query: str

@router.post("/agent-chat")
def agent_chat(request: AgentRequest):

    result = app_graph.invoke({
        "query": request.query
    })

    return result
