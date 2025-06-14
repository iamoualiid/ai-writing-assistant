import requests
from bs4 import BeautifulSoup

def scrape_article_text(url):
    """
    Scrape paragraph text from a given URL and return the combined content.
    Text is truncated to 5000 characters max.
    """
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'  # Ensure proper character decoding

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text() for p in paragraphs)

        return text[:5000]
    except Exception as e:
        print("Scraping error:", e)
        return ""
