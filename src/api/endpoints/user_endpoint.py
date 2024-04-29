from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from application.dto.user_dto import UserRegistrationDTO, UserUpdatePasswordDTO, DeleteUserDTO
from api.deps import get_db
from application.use_cases.user_use_cases import UserUseCases
from domain.models.user import User
from infrastructure.repositories.sql_user_repository import SQLUserRepository

router = APIRouter()

@router.post("/", response_model=User)
async def register(
        user_dto: UserRegistrationDTO,
        db: AsyncSession = Depends(get_db)
):
    user_repository = SQLUserRepository(db)
    user_service = UserUseCases(user_repository)
    new_user = await user_service.register(user_dto)
    return new_user

@router.get("/", response_model=List[User])
async def get_users(
        db: AsyncSession = Depends(get_db)
):
    user_repository = SQLUserRepository(db)
    user_service = UserUseCases(user_repository)
    users = await user_service.get_all()
    return users

@router.get("/{email}", response_model=User)
async def get_user(email: str,
                   db: AsyncSession = Depends(get_db)
):
    user_repository = SQLUserRepository(db)
    user_service = UserUseCases(user_repository)
    user = await user_service.get_by_email(email)
    return user

@router.put("/{email}", response_model=dict)
async def change_userpassword(updatepassword_dto: UserUpdatePasswordDTO,
                   db: AsyncSession = Depends(get_db)
):
    user_repository = SQLUserRepository(db)
    user_service = UserUseCases(user_repository)
    user = await user_service.update_password(updatepassword_dto)
    return {"message": "Password updated successfully"}

@router.delete("/{email}", response_model=dict)
async def remove_user(deleteuser_dto: DeleteUserDTO,
                   db: AsyncSession = Depends(get_db)
):
    user_repository = SQLUserRepository(db)
    user_service = UserUseCases(user_repository)
    user = await user_service.delete_user(deleteuser_dto)
    return {"message": "User deleted successfully"}
