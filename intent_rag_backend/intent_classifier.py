import torch
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

def classify_intent(text):
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs)
    return torch.argmax(outputs.logits, dim=1).item()

if __name__ == "__main__":
    print(classify_intent("turn on the lights"))
