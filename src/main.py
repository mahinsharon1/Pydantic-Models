from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class User(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8)


@app.post("/register")
def register_user(user: User):
    return {
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email
    }