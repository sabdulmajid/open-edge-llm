import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)

class IntentRouter:
    """
    IntentRouter classifies user utterances into smart home intents or fallback actions.
    Integrates with a HuggingFace Transformers model for intent classification.
    """
    def __init__(self, model_name: str = 'cross-encoder/nli-deberta-v3-base'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.labels = ["turn_on_lights", "turn_off_lights", "weather_query", "fallback"]

    def route(self, text: str) -> Dict[str, Any]:
        """
        Classify the intent of the input text and return a structured action dict.
        """
        # Example intent prompts for zero-shot classification
        candidate_labels = [
            "turn on the lights",
            "turn off the lights",
            "what is the weather",
            "other"
        ]
        classifier = pipeline(
            "zero-shot-classification",
            model=self.model,
            tokenizer=self.tokenizer
        )
        result = classifier(text, candidate_labels)
        label = result['labels'][0]
        score = result['scores'][0]
        logging.info(f"Intent: {label} (score={score:.2f})")
        if label == "turn on the lights" and score > 0.7:
            return {"action": "turn_on_lights", "confidence": score}
        elif label == "turn off the lights" and score > 0.7:
            return {"action": "turn_off_lights", "confidence": score}
        elif label == "what is the weather" and score > 0.7:
            return {"action": "weather_query", "confidence": score}
        else:
            return {"action": "fallback", "confidence": score}

if __name__ == "__main__":
    router = IntentRouter()
    print(router.route("turn on the lights in the kitchen"))
    print(router.route("is it raining outside?"))
    print(router.route("turn off the bedroom lights"))
    print(router.route("play some music"))
