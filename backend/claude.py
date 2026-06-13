from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def start_interview(interview_type: str, difficulty: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "system",
            "content": f"""You are a friendly but professional interviewer conducting a {difficulty} level {interview_type} interview. 
Ask ONE conversational question at a time — not coding problems.
For HR: ask about experience, strengths, teamwork, goals.
For DSA: ask candidate to EXPLAIN concepts verbally, not write code.
For System Design: ask how they would design something, discuss tradeoffs.
Keep it natural like a real conversation. Start by greeting the candidate and asking your first question."""
        }, {
            "role": "user",
            "content": "Start the interview."
        }]
    )
    return response.choices[0].message.content

def chat_interview(history: list, user_message: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history + [{
            "role": "user",
            "content": user_message
        }]
    )
    return response.choices[0].message.content

def evaluate_interview(history: list) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history + [{
            "role": "user",
            "content": """The interview is now over. Please evaluate the candidate's overall performance.
Give your response in this exact format:

Overall Score: X/10

Strengths:
- (point 1)
- (point 2)

Areas to Improve:
- (point 1)
- (point 2)

Final Verdict: (1-2 lines — would you hire this candidate?)"""
        }]
    )
    return response.choices[0].message.content