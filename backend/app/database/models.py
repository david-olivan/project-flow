from beanie import Document
from pydantic import EmailStr, BaseModel
from typing import Optional


class API_Key(BaseModel):
    api_key: str
    role: str


class User(Document):
    name: str
    last_name: str
    email: EmailStr
    password: str

    api_key: Optional[API_Key] = None

    class Settings:
        name = "users"
