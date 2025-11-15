from pydantic import BaseModel
from beanie import PydanticObjectId


class ProjectRequest(BaseModel):
    name: str
    team: str


class ProjectResponse(BaseModel):
    id: PydanticObjectId
    name: str
    team: str
