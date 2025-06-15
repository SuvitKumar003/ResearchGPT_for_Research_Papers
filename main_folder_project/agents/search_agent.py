# agents/search_agent.py
import arxiv

def search_arxiv(topic: str, max_results: int = 10) -> list[str]:
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    return [result.summary for result in search.results()]
