from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.ai_agent import JBVPAgent

app = FastAPI(title="JBVP AI Agent API", version="0.1.0")
agent = JBVPAgent(data_dir="data")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class AssignmentRequest(BaseModel):
    topic: str
    mode: str = "assignment_help"


class QuestionPaperRequest(BaseModel):
    subject: str
    total_questions: int = 10


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/chat")
def chat(payload: ChatRequest) -> dict:
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    return {"reply": agent.chat(payload.message)}


@app.post("/notes/summarize")
def summarize(payload: ChatRequest) -> dict:
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Input cannot be empty")
    return {"summary": agent.summarize(payload.message)}


@app.post("/assignment")
def assignment(payload: AssignmentRequest) -> dict:
    if not payload.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    return {"result": agent.assignment_help(payload.topic, payload.mode)}


@app.post("/college-info")
def college_info(payload: ChatRequest) -> dict:
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    return {"info": agent.college_info(payload.message)}


@app.post("/question-paper")
def question_paper(payload: QuestionPaperRequest) -> dict:
    if payload.total_questions <= 0:
        raise HTTPException(status_code=400, detail="total_questions must be positive")
    return {
        "subject": payload.subject,
        "questions": agent.generate_question_paper(
            payload.subject,
            payload.total_questions,
        ),
    }
