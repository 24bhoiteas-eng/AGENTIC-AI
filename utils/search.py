# utils/search.py

from tavily import TavilyClient   # Line 1
import os                          # Line 2
from dotenv import load_dotenv     # Line 3

load_dotenv()                      # Line 4

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))  # Line 5

def search_brand(query: str, max_results: int = 5) -> str:  # Line 6
    """
    Search for information about a brand using Tavily.
    Returns a single string of combined search results.
    """
    try:
        response = client.search(                           # Line 7
            query=query,
            search_depth="advanced",
            max_results=max_results
        )
        results = []                                        # Line 8
        for item in response.get("results", []):            # Line 9
            title = item.get("title", "")
            content = item.get("content", "")
            url = item.get("url", "")
            results.append(f"Source: {url}\nTitle: {title}\nContent: {content}\n")

        return "\n---\n".join(results)                      # Line 10

    except Exception as e:
        return f"Search error: {str(e)}"                   # Line 11