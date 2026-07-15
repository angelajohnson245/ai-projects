## AI Use Cases — Learning Journey (Week-by-Week Progress)
Welcome to my AI Use Cases Learning Repository — a structured, week‑by‑week collection of hands‑on exercises, experiments, and mini‑projects as I learn and practice modern AI development.
This repo documents my daily progress as I explore:
Large Language Models (LLMs)
Prompt engineering
Python automation
AI system design
Virtual environments & dependency management
Real-world AI use cases

## Repository Structure
The project is organized by weeks and days, making it easy to follow my learning path:
Code:
ai-usecases/
│
└── week1/
    ├── day1/
    ├── day2/
    ├── day3/
    └── day4/
Each dayX folder contains:

Python scripts (main.py, hello_llm.py, etc.)
A dedicated virtual environment
Supporting files (pyproject.toml, .python-version, etc.)
Notes and experiments for that day
This structure keeps each day isolated so I can experiment freely without breaking other exercises.

## What I’m Learning
Week 1 — Foundations
Setting up Python environments
Understanding LLM basics
Writing simple AI scripts
Exploring system prompts
Building small AI-driven utilities
More weeks will be added as I continue learning.

## Tech Stack
Python 3.x
Virtual Environments (.venv)
LLM-based scripts
Prompt engineering
VS Code
Git & GitHub

## Project Hygiene
This repo follows clean development practices:
Virtual environments are ignored using .gitignore
Local notes are excluded
No secrets or .env files are committed
Only source code and learning artifacts are pushed



## How to use:
PS C:\ai-usecases> cd week1                               
PS C:\ai-usecases\week1> cd day4                                
PS C:\ai-usecases\week1\day4> .venv\scripts\activate                 
(day4) PS C:\ai-usecases\week1\day4> python .\json_pydantic_model_usecase.py

# Output:
{
  "name": "Angela",
   "order_number": "123456",
   "email_address": "angela@example.com",
   "phone_number": "+1234567890"
}
