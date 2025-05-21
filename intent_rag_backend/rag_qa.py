import torch
from transformers import pipeline

qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

def answer_question(question, context):
    return qa_pipeline(question=question, context=context)

if __name__ == "__main__":
    context = "The stove was last turned off at 8pm."
    question = "Did I leave the stove on?"
    print(answer_question(question, context))
