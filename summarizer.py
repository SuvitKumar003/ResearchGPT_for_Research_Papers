from transformers import pipeline

class Summarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="t5-base", framework="pt")

    def summarize(self, text):
        if len(text.split()) < 50:
            return text
        summary = self.summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']
