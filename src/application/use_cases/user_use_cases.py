from typing import List

from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from application.dto.user_dto import UserRegistrationDTO


class UserUseCases:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register(self, user_dto: UserRegistrationDTO) -> User:
        # Placeholder for password hashing logic
        hashed_password = user_dto.password + "_hashed"

        user = User(username=user_dto.username, email=user_dto.email, hashed_password=hashed_password)
        await self.user_repository.add(user)
        return user

    async def get_all(self) -> List[User]:
        users = await self.user_repository.get_all()
        return users
    
    async def get_by_email(self, email:str) -> User:
        user = await self.user_repository.get_by_email(email)
        return user
    
    async def update_user(self, email:str, password:str)-> None:
        hashed_password = password + "_hashed"
        await self.user_repository.update_user(email, hashed_password)

    async def delete_user(self, email:str) -> None:
        await self.user_repository.delete_user(email)



        