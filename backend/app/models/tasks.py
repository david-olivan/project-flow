from pydantic import BaseModel, EmailStr, Field, field_validator
from beanie import PydanticObjectId
from typing import Optional, List
from datetime import datetime


class TaskRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Task name")
    priority: str = Field(..., pattern="^(low|medium|high)$", description="Task priority: low, medium, or high")
    belongs_to: PydanticObjectId
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = Field(None, max_length=1000, description="Task notes")
    effort: Optional[float] = Field(None, ge=0, le=1000, description="Effort in hours")
    assigned_to: Optional[List[EmailStr]] = []

    @field_validator('end_date')
    @classmethod
    def validate_dates(cls, end_date, info):
        if end_date and info.data.get('start_date') and end_date < info.data['start_date']:
            raise ValueError('end_date must be after start_date')
        return end_date


class TaskResponse(BaseModel):
    id: PydanticObjectId
    name: str
    priority: str
    belongs_to: PydanticObjectId
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = None
    effort: Optional[float] = None
    assigned_to: Optional[List[EmailStr]] = []
