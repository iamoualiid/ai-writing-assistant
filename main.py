from tools.serper_tool import search_google
from tools.scraper_tool import scrape_article_text
from tools.file_read_tool import read_pdf

from agents.summary_agent import summarize_text
from agents.keyword_agent import extract_keywords
from agents.pdf_agent import match_summary_with_pdf

import json

if __name__ == "__main__":
    topic = "Nouveautés en énergies renouvelables 2025"

    # Step 1: Search for a relevant article using Serper API
    results = search_google(topic)
    if not results:
        print("No search results found.")
        exit()

    article = results[0]
    url = article["link"]
    titre = article["title"]

    # Step 2: Scrape article text from the selected URL
    article_text = scrape_article_text(url)
    if not article_text:
        print("Failed to extract article content.")
        exit()

    # Step 3: Summarize the article
    resume = summarize_text(article_text)

    # Step 4: Extract keywords from the article
    mots_cles = extract_keywords(article_text)

    # Step 5: Read and extract content from the reference PDF
    pdf_data = read_pdf("reference.pdf")
    if not pdf_data:
        print("Failed to read the PDF file.")
        exit()

    # Step 6: Match the article summary with the most relevant PDF page(s)
    matched_refs = match_summary_with_pdf(resume, pdf_data)

    # Step 7: Build and save final structured output
    final_output = {
        "titre_article": titre,
        "resume": resume,
        "mots_cles": mots_cles,
        "liens_references_pdf": matched_refs,
        "url_source": url
    }

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    print("Final result saved to output.json.")
