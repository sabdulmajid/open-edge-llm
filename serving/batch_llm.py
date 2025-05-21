import torch
from transformers import pipeline

# Example: batch inference for serving
class BatchLLM:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')
    def generate(self, prompts):
        return [self.generator(prompt, max_length=30)[0]['generated_text'] for prompt in prompts]

if __name__ == "__main__":
    llm = BatchLLM()
    print(llm.generate(["Hello, world!", "Edge AI is..."]))
