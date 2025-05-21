import os
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
)
from typing import List, Dict

class TextDataset(Dataset):
    def __init__(self, texts: List[str], tokenizer, block_size: int = 512):
        self.examples = []
        for text in texts:
            tokenized = tokenizer(text, truncation=True, max_length=block_size, padding="max_length")
            self.examples.append({k: torch.tensor(v) for k, v in tokenized.items()})
    def __len__(self):
        return len(self.examples)
    def __getitem__(self, i):
        return self.examples[i]

def load_training_data(data_path: str) -> List[str]:
    with open(data_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def finetune(
    model_name: str = 'meta-llama/Llama-2-7b-hf',
    data_path: str = 'train.txt',
    output_dir: str = './finetuned-llama',
    epochs: int = 2,
    batch_size: int = 2,
    lr: float = 5e-5,
    block_size: int = 256
):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    texts = load_training_data(data_path)
    dataset = TextDataset(texts, tokenizer, block_size)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        save_steps=100,
        save_total_limit=2,
        prediction_loss_only=True,
        learning_rate=lr,
        logging_steps=10,
        report_to=[],
        fp16=torch.cuda.is_available(),
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )
    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Finetuned model saved to {output_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Finetune Llama-2 on your data.")
    parser.add_argument('--model_name', type=str, default='meta-llama/Llama-2-7b-hf')
    parser.add_argument('--data_path', type=str, default='train.txt')
    parser.add_argument('--output_dir', type=str, default='./finetuned-llama')
    parser.add_argument('--epochs', type=int, default=2)
    parser.add_argument('--batch_size', type=int, default=2)
    parser.add_argument('--lr', type=float, default=5e-5)
    parser.add_argument('--block_size', type=int, default=256)
    args = parser.parse_args()
    finetune(
        model_name=args.model_name,
        data_path=args.data_path,
        output_dir=args.output_dir,
        epochs=args.epochs,
        batch_size=args.batch_size,
        lr=args.lr,
        block_size=args.block_size
    )
