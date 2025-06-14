from sentence_transformers import SentenceTransformer, util

# Load the sentence similarity model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def match_summary_with_pdf(summary, pdf_pages, top_k=1):
    """
    Compare the summary to each page in the PDF and return the top_k most relevant pages.
    Each match includes a short excerpt and its corresponding page number.
    """
    summary_embedding = model.encode(summary, convert_to_tensor=True)

    results = []
    for page in pdf_pages:
        page_embedding = model.encode(page["text"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(summary_embedding, page_embedding).item()

        results.append({
            "page": page["page"],
            "text": page["text"],
            "score": score
        })

    top_matches = sorted(results, key=lambda x: x["score"], reverse=True)[:top_k]

    return [
        {
            "extrait": match["text"][:300],
            "page": match["page"]
        }
        for match in top_matches
    ]
