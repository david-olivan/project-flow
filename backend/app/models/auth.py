from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict
from beanie import PydanticObjectId


class UserRequest(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: PydanticObjectId
    name: str
    last_name: str
    email: EmailStr
