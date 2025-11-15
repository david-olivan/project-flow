from fastapi import APIRouter, status, HTTPException, Depends
from beanie import PydanticObjectId
from typing import List

from ..database.models import Task, Project, User
from ..models.tasks import TaskRequest, TaskResponse
from ..controllers.auth import get_api_key_from_header, validate_api_key

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
async def create_task(
    task: TaskRequest,
    api_key: str = Depends(get_api_key_from_header)
):
    role = await validate_api_key(api_key)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    # Verify project exists
    project = await Project.get(task.belongs_to)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {task.belongs_to} not found"
        )

    # Verify all assigned users exist
    if task.assigned_to:
        for email in task.assigned_to:
            user = await User.find_one(User.email == email)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User with email {email} not found"
                )

    # Create task with Link to project
    new_task = Task(
        name=task.name,
        priority=task.priority,
        belongs_to=project,
        start_date=task.start_date,
        end_date=task.end_date,
        notes=task.notes,
        effort=task.effort,
        assigned_to=task.assigned_to
    )
    await new_task.create()

    return TaskResponse(
        id=new_task.id,
        name=new_task.name,
        priority=new_task.priority,
        belongs_to=task.belongs_to,
        start_date=new_task.start_date,
        end_date=new_task.end_date,
        notes=new_task.notes,
        effort=new_task.effort,
        assigned_to=new_task.assigned_to
    )


@router.get("/", response_model=List[TaskResponse])
async def get_tasks(api_key: str = Depends(get_api_key_from_header)):
    role = await validate_api_key(api_key)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    tasks = await Task.find_all().to_list()

    return [
        TaskResponse(
            id=task.id,
            name=task.name,
            priority=task.priority,
            belongs_to=task.belongs_to.ref.id if hasattr(task.belongs_to, 'ref') else task.belongs_to.id,
            start_date=task.start_date,
            end_date=task.end_date,
            notes=task.notes,
            effort=task.effort,
            assigned_to=task.assigned_to
        )
        for task in tasks
    ]
