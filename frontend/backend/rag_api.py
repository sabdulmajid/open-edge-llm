from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    context: str

@app.post("/rag-qa/")
async def rag_qa(req: QueryRequest):
    # Placeholder: call RAG pipeline
    return {"answer": f"Pretend answer to: {req.question}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
