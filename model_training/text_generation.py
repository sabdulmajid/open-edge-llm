import torch
from transformers import pipeline

text_generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    return text_generator(prompt, max_length=50)[0]['generated_text']

if __name__ == "__main__":
    prompt = "Smart home assistant:"
    print(generate_text(prompt))
