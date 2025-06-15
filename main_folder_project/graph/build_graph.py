from langgraph.graph import StateGraph
from typing import TypedDict, List
from agents.search_agent import search_arxiv
from agents.summarizer_agent import summarize
from agents.reporter_agent import reporter_agent

class GraphState(TypedDict):
    topic: str
    papers: List[str]
    summaries: List[str]
    report: str

def retrieve_papers(state: GraphState) -> dict:
    return {"papers": search_arxiv(state["topic"])}

def summarize_papers(state: GraphState) -> dict:
    return {"summaries": [summarize(p) for p in state["papers"]]}

def report_agent(state: GraphState) -> dict:
    return {"report": reporter_agent(state)}

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("search", retrieve_papers)
    builder.add_node("summarize", summarize_papers)
    builder.add_node("reporter", report_agent)  # renamed node

    builder.set_entry_point("search")
    builder.add_edge("search", "summarize")
    builder.add_edge("summarize", "reporter")
    builder.set_finish_point("reporter")

    return builder.compile()
