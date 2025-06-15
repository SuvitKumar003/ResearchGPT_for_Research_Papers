from langgraph.graph import StateGraph
from langchain.agents import Tool
from langchain_app.agents.search_tool import search_papers
from langchain_app.agents.summarize_tool import summarize_text
from langchain_app.agents.critic_tool import critique_summary
from langchain_app.agents.synth_tool import synthesize_insights

# Define tools
tools = [
    Tool(name="SearchPapers", func=search_papers),
    Tool(name="SummarizeText", func=summarize_text),
    Tool(name="CritiqueSummary", func=critique_summary),
    Tool(name="SynthesizeInsights", func=synthesize_insights),
]

# Create LangGraph graph
def run_graph(query: str):
    state = {"input": query}
    graph = StateGraph()

    graph.add_node("search", search_papers)
    graph.add_node("summarize", summarize_text)
    graph.add_node("critic", critique_summary)
    graph.add_node("synthesize", synthesize_insights)

    graph.set_entry_point("search")
    graph.add_edge("search", "summarize")
    graph.add_edge("summarize", "critic")
    graph.add_edge("critic", "synthesize")

    graph.set_finish_point("synthesize")

    app = graph.compile()
    return app.invoke(state)["output"]
