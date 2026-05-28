from typing import TypedDict
from langgraph.graph import StateGraph

from app.agents.research_agent import research_agent
from app.agents.rag_agent import rag_agent
from app.agents.report_agent import report_agent


class AgentState(TypedDict):
    query: str
    research: str
    rag_response: str
    report: str


builder = StateGraph(AgentState)



def run_research(state):
    result = research_agent(state["query"])
    return {"research": result}



def run_rag(state):
    result = rag_agent(state["query"])
    return {"rag_response": result}



def run_report(state):
    final_report = report_agent(
        state["research"] + "\n" + state["rag_response"]
    )
    return {"report": final_report}


builder.add_node("research", run_research)
builder.add_node("rag", run_rag)
builder.add_node("report", run_report)

builder.set_entry_point("research")

builder.add_edge("research", "rag")
builder.add_edge("rag", "report")

workflow = builder.compile()
