from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer('all-MiniLM-L6-v2')
kw_model = KeyBERT(model)

def extract_keywords(text, top_n=5):
    """
    Extract key phrases from a given text using KeyBERT.
    Returns a list of the top_n keywords.
    """
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        use_maxsum=True,
        nr_candidates=20,
        top_n=top_n
    )
    return [kw[0] for kw in keywords]
