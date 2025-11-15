from pydantic import BaseModel, EmailStr
from beanie import PydanticObjectId
from typing import Optional, List
from datetime import datetime


class TaskRequest(BaseModel):
    name: str
    priority: str
    belongs_to: PydanticObjectId
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = None
    effort: Optional[float] = None
    assigned_to: Optional[List[EmailStr]] = []


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
