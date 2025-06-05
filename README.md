# Book Review API

A RESTful API built with Django and Django REST Framework that allows users to manage books and submit reviews.

---

## Features

- Full CRUD operations for books
- User-submitted reviews with ratings and comments
- Token-based authentication
- Interactive API documentation (Swagger / ReDoc)

## Installation

```bash
# Clone the repository
git clone https://github.com/paulosergioveras/BookAPI.git
cd BOOKAPI

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

---

## API Documentation

- Swagger UI: [`/swagger/`](http://localhost:8000/swagger/)
- ReDoc: [`/redoc/`](http://localhost:8000/redoc/)
- OpenAPI Schema (JSON): [`/swagger.json`](http://localhost:8000/swagger.json)

---

## Authentication

This API uses token-based authentication. To obtain a token:

1. Create a user via `/admin/` or a registration endpoint (if available).
2. Make a `POST` request to `/api/token/` with your credentials:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```