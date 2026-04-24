# utils/search.py

from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_topic(query: str, max_results: int = 5) -> str:
    """
    Search for information about a topic using Tavily.
    Returns a single string of combined search results.
    """
    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results
        )
        results = []
        for item in response.get("results", []):
            title = item.get("title", "")
            content = item.get("content", "")
            url = item.get("url", "")
            results.append(f"Source: {url}\nTitle: {title}\nContent: {content}\n")

        return "\n---\n".join(results)

    except Exception as e:
        return f"Search error: {str(e)}"