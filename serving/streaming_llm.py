import torch
from transformers import pipeline

# Example: streaming text generation for vLLM-like serving
class StreamingLLM:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')
    def stream(self, prompt):
        for i in range(1, 4):
            yield self.generator(prompt, max_length=10*i)[0]['generated_text']

if __name__ == "__main__":
    llm = StreamingLLM()
    for chunk in llm.stream("Edge-to-cloud AI is"): print(chunk)
