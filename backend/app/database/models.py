from beanie import Document, Link, BackLink
from pydantic import EmailStr, BaseModel
from typing import Optional, List
from datetime import datetime


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


class Project(Document):
    name: str
    team: str

    class Settings:
        name = "projects"


class Task(Document):
    name: str
    priority: str
    belongs_to: Link[Project]
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = None
    effort: Optional[float] = None
    assigned_to: Optional[List[EmailStr]] = []

    class Settings:
        name = "tasks"
