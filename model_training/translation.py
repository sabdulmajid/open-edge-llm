import torch
from transformers import pipeline

translator = pipeline('translation_en_to_fr', model='t5-base')

def translate(text):
    return translator(text)[0]['translation_text']

if __name__ == "__main__":
    print(translate("Hello, how are you?"))
