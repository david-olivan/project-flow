from fastapi import APIRouter, status, HTTPException, status, Depends
from beanie import PydanticObjectId

from ..database.models import User
from ..models.auth import UserRequest, UserResponse
from ..controllers.auth import (
    generate_and_save_api_key,
    validate_api_key,
    get_api_key_from_header,
)

router = APIRouter(prefix="/auth", tags=["API Key"])

roles = ["admin", "user", "test"]


@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserRequest):
    # Check if user with this email already exists
    existing_user = await User.find_one(User.email == user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email {user.email} already exists"
        )

    # TODO: Hash password before storing (use bcrypt or argon2)
    # Currently storing passwords in plain text - SECURITY RISK!
    nuevo_usuario = await User(**user.model_dump()).create()
    return nuevo_usuario


@router.post("/new_key/{user_id}", status_code=status.HTTP_201_CREATED)
async def create_new_api_key(user_id: PydanticObjectId, role: str):
    if role not in roles:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    user = await User.get(user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    api_key = await generate_and_save_api_key(role=role, user=user)

    return api_key


@router.get("/me")
async def get_current_user(api_key: str = Depends(get_api_key_from_header)):
    role = await validate_api_key(api_key)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )
    return {"role": role}
