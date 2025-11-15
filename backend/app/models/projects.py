from pydantic import BaseModel, Field
from beanie import PydanticObjectId


class ProjectRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Project name")
    team: str = Field(..., min_length=1, max_length=100, description="Team name")


class ProjectResponse(BaseModel):
    id: PydanticObjectId
    name: str
    team: str
