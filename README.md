# 🎯 AI Mock Interview Coach

A full-stack conversational AI platform that helps students practice interviews in real-time. Powered by Groq's LLaMA 3.3 70B model, it conducts natural, back-and-forth interview conversations — not scripted Q&A — and adapts its difficulty based on how well you're answering.

🔗 **[Live Demo](https://tushar-alange.github.io/mock-interview-coach/)** • **[Backend API Docs](https://mock-interview-coach-1.onrender.com/docs)**

> ⚠️ **Backend Wake-Up Time**
>
> The backend is hosted on Render's free tier and may go to sleep after periods of inactivity. If the application hasn't been used recently, the first request can take **30–60 seconds** while the server starts up. Please wait a moment before beginning the interview.

---

## ✨ Features

- 🗣️ **Conversational Interviews** — Real back-and-forth dialogue, not static question banks
- 🎤 **Voice Input** — Speak your answers using the Web Speech API (Chrome)
- 📈 **Adaptive Difficulty** — Automatically adjusts question difficulty based on your answer quality
- ⏱️ **Live Timer** — 60-second countdown per question to simulate real interview pressure
- 📊 **AI-Generated Score Report** — Get an overall score, strengths, and areas to improve at the end
- 📄 **PDF Export** — Download your full interview transcript and evaluation
- 🎚️ **Multiple Interview Types** — HR, DSA, System Design, Python, JavaScript

---

## 🏗️ Architecture

```text
┌──────────────────┐      REST API      ┌───────────────────┐      API calls      ┌─────────────────┐
│     Frontend     │ ─────────────────▶ │      Backend      │ ──────────────────▶ │  Gemini API     │
│  HTML / CSS / JS │                    │  Python + FastAPI │                     │                 │
│ (GitHub Pages)   │ ◀───────────────── │     (Render)      │ ◀────────────────── │                 │
└──────────────────┘                    └───────────────────┘                     └─────────────────┘
```

**Flow:** User selects interview type and difficulty → Backend requests an opening question from Groq → User answers using text or voice → Full conversation history is sent with every request to maintain context → Groq generates follow-up questions → At the end, Groq evaluates the complete interview and returns a score with personalized feedback.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---------|------------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Backend | Python, FastAPI |
| AI Engine | Gemini API |
| Voice Input | Web Speech API |
| PDF Export | jsPDF |
| Backend Hosting | Render |
| Frontend Hosting | GitHub Pages |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
mock-interview-coach/
├── index.html
├── frontend/
│   └── index.html
├── backend/
│   ├── main.py
│   ├── claude.py
│   ├── requirements.txt
│   └── .env
└── .gitignore
```

---

> ⚠️ Voice input requires Google Chrome and a running server (not `file://`) because of browser security restrictions.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | `/start-interview` | Starts a new interview and returns the first question |
| POST | `/chat` | Sends the candidate's answer and returns the next AI response |
| POST | `/evaluate-interview` | Ends the interview and returns score, strengths, and improvement areas |

---

## 📈 How Adaptive Difficulty Works

After every response, a lightweight scoring mechanism evaluates answer quality:

- Short or vague answers → Difficulty decreases
- Detailed and well-structured answers → Difficulty increases
- Future questions are generated based on the updated difficulty level

This creates a more realistic interview experience tailored to the candidate's performance.

---
