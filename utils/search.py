import os
from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient

def get_api_key(key_name):
    """Reads from Streamlit secrets (cloud) or .env (local)."""
    try:
        import streamlit as st
        return st.secrets[key_name]
    except:
        return os.getenv(key_name)

def get_tavily_client():
    api_key = get_api_key("TAVILY_API_KEY")
    if not api_key:
        raise Exception("TAVILY_API_KEY not found in secrets or .env file!")
    return TavilyClient(api_key=api_key)

def search_topic(query: str, max_results: int = 5) -> str:
    """
    Search for information about a topic using Tavily.
    Returns a single string of combined search results.
    """
    try:
        client = get_tavily_client()
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
