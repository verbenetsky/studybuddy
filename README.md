# StudyBuddy

A platform where students exchange used textbooks and book peer tutoring sessions.

## Stack

- Python 3.10
- FastAPI
- PostgreSQL (planned, not connected yet)
- pytest

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Run

```bash
fastapi dev app/main.py
```

The API will be available at http://localhost:8000.
Interactive API docs: http://localhost:8000/docs

## Tests

```bash
pytest
```

## Roadmap (not yet implemented)

- Tables: users, subjects, textbooks, exchange_requests, tutoring_sessions
- Endpoints: GET/POST textbooks, POST/PATCH exchange requests, GET/POST/DELETE tutoring sessions
- Error handling: 404, 422, 409 (double booking / already exchanged textbook)
