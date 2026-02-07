# FastAPI JWT Authentication API

A REST API built with FastAPI featuring JWT token-based authentication, SQLAlchemy ORM, and SQLite.

## API Endpoints

| Method | Path             | Auth | Description        |
|--------|------------------|------|--------------------|
| GET    | `/health`        | No   | Health check       |
| POST   | `/auth/register` | No   | Create new user    |
| POST   | `/auth/login`    | No   | Get JWT token      |
| GET    | `/auth/me`       | Yes  | Get current user   |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn src.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive Swagger UI.

## Test

```bash
pytest tests/ -v
```

## Project Structure

```
src/
├── main.py                  # FastAPI app entry point
├── config.py                # Settings via pydantic-settings
├── database.py              # SQLAlchemy engine, session, Base
├── models.py                # User ORM model
├── schemas.py               # Pydantic request/response schemas
├── auth.py                  # Password hashing, JWT create/verify
└── routes/
    └── auth_routes.py       # Register, login, /me endpoints
tests/
├── conftest.py              # Test client fixture, in-memory SQLite
└── test_auth.py             # 7 tests covering all endpoints
```

## Configuration

Settings are loaded from environment variables or a `.env` file:

| Variable                      | Default                           |
|-------------------------------|-----------------------------------|
| `DATABASE_URL`                | `sqlite:///./app.db`              |
| `SECRET_KEY`                  | `dev-secret-key-change-in-production` |
| `ALGORITHM`                   | `HS256`                           |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30`                              |

## Dev Tools

- **Formatter**: Black
- **Linter**: Ruff
- **Type Checking**: mypy
- **Testing**: pytest
