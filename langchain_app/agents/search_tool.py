from langchain.agents import tool
from langchain_app.chains.rag_chain import get_relevant_docs

@tool
def search_papers(query: str) -> str:
    """Search research papers relevant to a query using RAG."""
    return get_relevant_docs(query)
