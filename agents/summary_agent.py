from transformers import pipeline, AutoTokenizer
from dotenv import load_dotenv
import os
import unicodedata

# Load environment variables
load_dotenv()

# Load summarization pipeline and tokenizer
MODEL_NAME = "facebook/bart-large-cnn"
summarizer = pipeline(
    "summarization",
    model=MODEL_NAME,
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def summarize_text(text):
    """
    Summarize a given text using the BART model.
    Input text is normalized and truncated to fit the model's token limit.
    """
    text = unicodedata.normalize("NFKD", text)

    # Tokenize and truncate to max 1024 tokens
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
    safe_text = tokenizer.decode(inputs["input_ids"][0], skip_special_tokens=True)

    summary = summarizer(
        safe_text,
        max_length=180,
        min_length=60,
        do_sample=False
    )
    return summary[0]['summary_text']
