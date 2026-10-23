# Music API

A secure and scalable RESTful backend for managing songs, artists, and playlists —
built with Django REST Framework and JWT authentication.

## Stack

- Django 5.1.1
- Django REST Framework
- djangorestframework-simplejwt (JWT)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# required: set a secret key (never commit the real one)
export DJANGO_SECRET_KEY="your-secret-key"
# optional
export DJANGO_DEBUG="1"
export DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET/POST | `/music/` | List / create tracks (paginated, auth required) |
| GET/PUT/DELETE | `/music/<id>/` | Retrieve / update / delete a track |
| POST | `/token/` | Obtain JWT access + refresh tokens |
| POST | `/token/refresh/` | Refresh the access token |

All `/music/` endpoints require a valid JWT access token
(`Authorization: Bearer <access_token>`).

## Notes

- `db.sqlite3` is the local dev database and is intentionally not tracked.
- Copy `.env.example` to `.env` for local configuration (see `.gitignore`).
