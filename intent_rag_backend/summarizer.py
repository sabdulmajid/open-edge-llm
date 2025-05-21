import torch
from transformers import pipeline

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

def summarize(text):
    return summarizer(text, max_length=50, min_length=10, do_sample=False)[0]['summary_text']

if __name__ == "__main__":
    text = "OpenEdge-LLM is a platform for edge-to-cloud multimodal AI assistants. It supports data ingestion, model training, and more."
    print(summarize(text))
