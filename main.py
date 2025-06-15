from fastapi import FastAPI
from app.services import summarize, qna, learnpath
from app.utils.blockchain import verify_request

app = FastAPI(title="LangChain AI Service")

@app.get("/")
def home():
    return {"status": "LangChain AI Service running."}

@app.post("/summarize")
def summarize_text(payload: dict):
    text = payload.get("text", "")
    verify_request(text)  # Mock blockchain
    return summarize.run(text)

@app.post("/ask")
def question_answer(payload: dict):
    context = payload.get("context", "")
    question = payload.get("question", "")
    verify_request(question)
    return qna.run(context, question)

@app.post("/learnpath")
def generate_learning_path(payload: dict):
    topic = payload.get("topic", "")
    verify_request(topic)
    return learnpath.run(topic)
