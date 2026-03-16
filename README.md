# JBVP AI Agent (Web AI)

A starter full-stack web project for JBVP students:

- Student chat for B.Pharm notes and concepts.
- Notes summarization endpoint.
- Assignment and viva help endpoint.
- College info assistant endpoint.
- Random question paper generator.

## Project structure

```text
jbvp-ai
├ backend
│  ├ ai_agent.py
│  └ main.py
├ data
└ frontend
   ├ index.html
   ├ script.js
   └ style.css
```

## Run backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
uvicorn backend.main:app --reload
```

## Run frontend

Open `frontend/index.html` in browser and use the UI.

> Note: the frontend is configured to call `http://127.0.0.1:8000`.
