from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Use Long T5 fine-tuned for long-document summarization
:contentReference[oaicite:5]{index=5}
:contentReference[oaicite:6]{index=6}

hf_pipe = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    max_length=512,
    min_length=150,
    do_sample=False
)
:contentReference[oaicite:7]{index=7}

:contentReference[oaicite:8]{index=8}
    :contentReference[oaicite:9]{index=9}
    :contentReference[oaicite:10]{index=10}
    :contentReference[oaicite:11]{index=11}
        :contentReference[oaicite:12]{index=12}
    :contentReference[oaicite:13]{index=13}
