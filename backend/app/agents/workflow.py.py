from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.agents.agents import (
    retrieval_agent,
    research_agent,
    summarizer_agent
)

class AgentState(TypedDict):

    query: str
    retrieved_data: str
    research_output: str
    final_output: str

workflow = StateGraph(AgentState)

workflow.add_node("retrieval", retrieval_agent)
workflow.add_node("research", research_agent)
workflow.add_node("summary", summarizer_agent)

workflow.set_entry_point("retrieval")

workflow.add_edge("retrieval", "research")
workflow.add_edge("research", "summary")
workflow.add_edge("summary", END)

app_graph = workflow.compile()