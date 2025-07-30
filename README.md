# FastAPI Todo App with JWT Authentication

## Overview

A secure Todo application backend built with FastAPI featuring JWT authentication, allowing users to register, login, and manage their todos with full CRUD functionality.

## Features

- ✅ JWT Authentication (OAuth2 password flow)
- ✅ User registration and login
- ✅ Protected todo operations
- ✅ SQLAlchemy ORM integration
- ✅ Pydantic data validation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Authentication

#### Register New User
- **Endpoint**: `POST /register`
- **Content-Type**: `application/json`
- **Request**:
  ```json
  {
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
- **Response**:
  ```json
  {
    "username": "newuser",
    "email": "user@example.com",
    "id": 1,
    "is_active": true
  }
  ```

#### Login (Get Access Token)
- **Endpoint**: `POST /token`
- **Content-Type**: `application/x-www-form-urlencoded`
- **Form Data**:
  ```
  username: yourusername
  password: yourpassword
  ```
- **Response**:
  ```json
  {
    "access_token": "eyJhbGciOi...",
    "token_type": "bearer"
  }
  ```

### Todo Operations (All require authentication)

#### Create Todo
- **Endpoint**: `POST /todos/`
- **Headers**: `Authorization: Bearer <token>`
- **Request**:
  ```json
  {
    "title": "Learn FastAPI",
    "description": "Study authentication",
    "completed": false
  }
  ```
- **Response**:
  ```json
  {
    "title": "Learn FastAPI",
    "description": "Study authentication",
    "completed": false,
    "id": 1,
    "owner_id": 1
  }
  ```

#### Get All Todos
- **Endpoint**: `GET /todos/`
- **Headers**: `Authorization: Bearer <token>`
- **Response**:
  ```json
  [
    {
      "title": "Learn FastAPI",
      "description": "Study authentication",
      "completed": false,
      "id": 1,
      "owner_id": 1
    }
  ]
  ```

#### Update Todo
- **Endpoint**: `PUT /todos/{todo_id}`
- **Headers**: `Authorization: Bearer <token>`
- **Request**:
  ```json
  {
    "title": "Updated title",
    "completed": true
  }
  ```

#### Delete Todo
- **Endpoint**: `DELETE /todos/{todo_id}`
- **Headers**: `Authorization: Bearer <token>`
- **Response**: 204 No Content

## Environment Variables

Create a `.env` file:
```ini
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./todos.db
```

## Project Structure

```
todo-app/
├── api/
│   ├── routes/
│   │   ├── auth.py
│   │   └── todos.py
│   └── services/
│       ├── auth.py
│       └── todos.py
├── core/
│   ├── config.py
│   └── security.py
├── models/
│   └── models.py
├── schemas/
│   └── schemas.py
├── database.py
├── main.py
└── requirements.txt
```

## Testing with Postman

1. Import the [Postman collection](link-to-collection)
2. Set environment variables:
   - `base_url`: `http://localhost:8000`
   - `token`: (will be set after login)

## Deployment

For production deployment, consider:
- Using PostgreSQL instead of SQLite
- Setting up proper HTTPS
- Using environment variables for secrets
- Containerizing with Docker

## License

MIT