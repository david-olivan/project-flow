from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List, Dict
from beanie import PydanticObjectId


class UserRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="User's first name")
    last_name: str = Field(..., min_length=1, max_length=100, description="User's last name")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128, description="User password (min 8 characters)")

    # TODO: Implement more robust password policy using a dedicated library
    # Consider using password-validator or similar for:
    # - Configurable complexity requirements (uppercase, lowercase, special chars)
    # - Common password blacklist
    # - Password strength meter
    # - Customizable rules per deployment environment
    @field_validator('password')
    @classmethod
    def validate_password(cls, password):
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isalpha() for char in password):
            raise ValueError('Password must contain at least one letter')
        return password


class UserResponse(BaseModel):
    id: PydanticObjectId
    name: str
    last_name: str
    email: EmailStr
