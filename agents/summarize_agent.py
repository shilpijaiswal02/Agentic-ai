from transformers import pipeline
import textwrap

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text: str) -> str:
    chunks = textwrap.wrap(text, 1000)
    summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=120,
            min_length=40,
            do_sample=False
        )
        summaries.append(result[0]["summary_text"])

    return " ".join(summaries)
