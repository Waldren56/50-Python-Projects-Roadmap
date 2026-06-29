# 50 Python Projects — Learning Path

A repository documenting a full progression of Python projects, from solid fundamentals through complex systems and production deployment. Each project introduces new concepts on top of the previous one — the folder structure and commit history together tell the story of the learning path.

> Note: Level 1 projects (1-10, absolute fundamentals) are not included in this repo. The progression documented here starts at level 2.

## Project index

### 🟡 Level 2 — Solid foundations

| # | Project | Skills | Status |
|---|---------|--------|--------|
| 11 | [To-Do list with file persistence](./11-todo-file/) | `open()`, text file handling | ✅ Done |
| 12 | [Contact book (terminal CRUD)](./12-rubrica/) | dictionaries, JSON persistence | ✅ Done |
| 13 | [Multiple-choice quiz with scoring](./13-quiz/) | nested data structures, `try/except` | ✅ Done |
| 14 | Unit converter | dictionaries, modular functions | ⬜ To do |
| 15 | Text file analyzer | `collections.Counter` | ⬜ To do |
| 16 | Simple web scraper | `requests`, `BeautifulSoup` | ⬜ To do |
| 17 | QR code generator | `qrcode` library | ⬜ To do |
| 18 | Digital terminal clock | `datetime`, `time` | ⬜ To do |
| 19 | CSV → JSON converter | `csv`, `json` | ⬜ To do |
| 20 | Birthday reminder bot | `datetime`, conditional logic | ⬜ To do — **checkpoint** |

### 🟠 Level 3 — Intermediate

| # | Project | Skills | Status |
|---|---------|--------|--------|
| 21 | Personal expense tracker with charts | `pandas`, `matplotlib` | ⬜ To do |
| 22 | Weather app (external API) | `requests`, API keys, JSON | ⬜ To do |
| 23 | Calculator with GUI | `tkinter` | ⬜ To do |
| 24 | Hangman game | OOP, game state management | ⬜ To do |
| 25 | Habit tracker | `sqlite3` | ⬜ To do |
| 26 | Chart generator from CSV | `pandas`, `matplotlib`/`seaborn` | ⬜ To do |
| 27 | Login system with password hashing | `hashlib`, input validation | ⬜ To do |
| 28 | Terminal mini-blog (DB-backed CRUD) | `sqlite3`, OOP | ⬜ To do |
| 29 | Simple Telegram bot | `python-telegram-bot`, APIs | ⬜ To do |
| 30 | PDF ↔ text/image converter | `PyPDF2`, `Pillow` | ⬜ To do — **checkpoint** |

### 🔴 Level 4 — Advanced

| # | Project | Skills | Status |
|---|---------|--------|--------|
| 31 | Flask web blog/app | `Flask`, Jinja2 | ⬜ To do |
| 32 | REST API with FastAPI (equipment rental) | `FastAPI`, Pydantic | ⬜ To do |
| 33 | Advanced multi-page scraper | `Scrapy` / `requests` + `pandas` | ⬜ To do |
| 34 | Interactive dashboard | `Streamlit` / `Dash` | ⬜ To do |
| 35 | Simple recommendation system | `pandas`, cosine similarity | ⬜ To do |
| 36 | Basic image classifier | `TensorFlow`/`PyTorch`, CNN | ⬜ To do |
| 37 | Chatbot with simple NLP | `nltk` / `spaCy` | ⬜ To do |
| 38 | File system automation | `os`, `shutil`, `pathlib` | ⬜ To do |
| 39 | Parallel web scraper | `asyncio` / `multiprocessing` | ⬜ To do |
| 40 | Image editor with custom filters | `Pillow`/`OpenCV` | ⬜ To do — **checkpoint** |

### 🟣 Level 5 — Expert

| # | Project | Skills | Status |
|---|---------|--------|--------|
| 41 | Full-text search engine | indexing, `Whoosh`/Elasticsearch | ⬜ To do |
| 42 | Time series forecasting | `statsmodels`, `Prophet`, LSTM | ⬜ To do |
| 43 | Full-stack web app | `Django`, ORM, sessions | ⬜ To do |
| 44 | Text generator (transformer model) | `transformers` (Hugging Face) | ⬜ To do |
| 45 | Real-time facial recognition | `OpenCV`, `face_recognition` | ⬜ To do |
| 46 | Algorithmic trading bot | `pandas`, exchange APIs, backtesting | ⬜ To do |
| 47 | Automated ETL pipeline | `Airflow` / `Luigi` | ⬜ To do |
| 48 | Multi-agent system | `asyncio`, microservices | ⬜ To do |
| 49 | Scalable GraphQL API | `Graphene`/`Strawberry`, Redis | ⬜ To do |
| 50 | Custom Python library published on PyPI | packaging, `pytest`, CI/CD | ⬜ To do — **final checkpoint** |

## Repository structure

```
python-projects/
├── README.md
├── 11-todo-file/
│   └── main.py
├── 12-rubrica/
│   └── main.py
├── 13-quiz/
│   └── main.py
├── 14-unit-converter/
│   └── ...
└── ...
```

Each folder contains the project's code and, where useful, a short local README with project-specific notes.

## Progress checkpoints

Roughly every 10 projects, the repo includes a comparative review (structure, readability, error handling, data validation, security, robustness, maintainability) to document progress over time. The first checkpoint will cover projects 11–20.

## How to use this repo

It's not meant to be cloned and used as a library — it's a documented learning path. Each project is self-contained and runnable on its own:

```bash
cd 13-quiz
python main.py
```

Extras (Docker, AWS) will be applied to the more advanced projects once they're completed, rather than studied in isolation.
