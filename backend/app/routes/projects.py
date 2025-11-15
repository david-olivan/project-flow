from fastapi import APIRouter, status, HTTPException, Depends
from typing import List

from ..database.models import Project
from ..models.projects import ProjectRequest, ProjectResponse
from ..controllers.auth import get_api_key_from_header, validate_api_key

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProjectResponse)
async def create_project(
    project: ProjectRequest,
    api_key: str = Depends(get_api_key_from_header)
):
    role = await validate_api_key(api_key)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    new_project = Project(
        name=project.name,
        team=project.team
    )
    await new_project.create()

    return ProjectResponse(
        id=new_project.id,
        name=new_project.name,
        team=new_project.team
    )


@router.get("/", response_model=List[ProjectResponse])
async def get_projects(api_key: str = Depends(get_api_key_from_header)):
    role = await validate_api_key(api_key)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    projects = await Project.find_all().to_list()

    return [
        ProjectResponse(
            id=project.id,
            name=project.name,
            team=project.team
        )
        for project in projects
    ]
