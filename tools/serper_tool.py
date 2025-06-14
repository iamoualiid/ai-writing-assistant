import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def search_google(query, num_results=1):
    """
    Search Google using the Serper.dev API and return the top organic result(s).
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }
    data = { "q": query }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        results = response.json().get("organic", [])
        return results[:num_results]
    else:
        print("Serper API error:", response.status_code)
        return []
