# researchgpt/summarizer.py

from transformers import pipeline

# Load once
summarizer = pipeline("summarization", model="t5-base", framework="pt")

def summarize_text(text, max_length=100, min_length=30):
    if len(text.split()) < 50:
        return text  # Skip short texts

    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"[ERROR in summarization]: {e}"
