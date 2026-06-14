from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from claude import start_interview, chat_interview, evaluate_interview

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

class StartRequest(BaseModel):
    interview_type: str
    difficulty: str

class ChatRequest(BaseModel):
    history: list
    user_message: str

class EvaluateRequest(BaseModel):
    history: list

@app.post("/start-interview")
def start(req: StartRequest):
    response = start_interview(req.interview_type, req.difficulty)
    return {"message": response}

@app.post("/chat")
def chat(req: ChatRequest):
    response = chat_interview(req.history, req.user_message)
    return {"message": response}

@app.post("/evaluate-interview")
def evaluate(req: EvaluateRequest):
    response = evaluate_interview(req.history)
    return {"feedback": response}