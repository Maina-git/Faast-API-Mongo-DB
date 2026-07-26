# 🔐 FastAPI MongoDB Authentication API

A secure authentication API built with **FastAPI**, **MongoDB**, and **JWT**. This project provides user registration and login functionality with password hashing and JSON Web Token authentication.

## 🚀 Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing (Argon2)
- MongoDB Integration
- Environment Variable Configuration
- FastAPI Swagger Documentation
- Modular Project Structure

---

## 🛠 Tech Stack

- FastAPI
- Python 3.13+
- MongoDB Atlas / MongoDB Community
- Motor (Async MongoDB Driver)
- JWT (python-jose)
- Pydantic
- pwdlib (Argon2)
- Uvicorn

---

## 📂 Project Structure

```text
fastapi-auth/
│
├── app/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── routes/
│   │   └── auth.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   └── auth_service.py
│   │
│   └── utils/
│       ├── hashing.py
│       └── jwt_handler.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-auth.git
```

Navigate into the project

```bash
cd fastapi-auth
```

Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
MONGO_URL=your_mongodb_connection_string
DATABASE_NAME=fastapi_auth

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Run the Project

```bash
uvicorn app.main:app --reload
```

The server will start at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Register User

```
POST /auth/register
```

Request

```json
{
    "name":"Francis",
    "email":"francis@gmail.com",
    "password":"password123"
}
```

---

### Login User

```
POST /auth/login
```

Request

```json
{
    "email":"francis@gmail.com",
    "password":"password123"
}
```

Response

```json
{
    "access_token":"JWT_TOKEN",
    "token_type":"bearer"
}
```

---

## Dependencies

```
FastAPI
Motor
MongoDB
python-jose
pwdlib
argon2-cffi
python-dotenv
uvicorn
pydantic
```

---

## Future Improvements

- Refresh Tokens
- Email Verification
- Password Reset
- Role-Based Authentication
- User Profile
- Docker Support
- Unit Testing
- Logging
- Rate Limiting
- OAuth Login (Google & GitHub)

---

## Author

**Francis Mainaa**

GitHub: https://github.com/Maina-git

LinkedIn: https://www.linkedin.com/in/francis-mainaa-2116342b2/

---

## License

This project is licensed under the MIT License.















