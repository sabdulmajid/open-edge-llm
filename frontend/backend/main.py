# FastAPI backend with simple chat endpoint
import os
import sys
from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel

# allow importing modules from repository root
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from intent_rag_backend.intent_router import IntentRouter
from intent_rag_backend.rag_qa import answer_question
from intent_rag_backend.summarizer import summarize

app = FastAPI()
router = IntentRouter()
conversation_history: List[Dict[str, str]] = []

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/history")
def history():
    return conversation_history[-10:]

@app.post("/chat")
def chat(req: ChatRequest):
    """Route user text to the proper handler and return a fun reply."""
    intent = router.route(req.message)
    if intent["action"] == "turn_on_lights":
        reply = "Lights turned on."
    elif intent["action"] == "turn_off_lights":
        reply = "Lights turned off."
    elif intent["action"] == "weather_query":
        reply = "It's always sunny in the demo!"
    else:
        rag_result = answer_question(req.message, "The stove was last turned off at 8pm.")
        reply = rag_result.get("answer", "I am not sure.")
    summary = summarize(reply)
    conversation_history.append({"user": req.message, "bot": summary})
    return {"answer": summary, "action": intent["action"]}
