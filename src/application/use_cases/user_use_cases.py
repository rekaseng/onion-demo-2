from typing import List

from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from application.dto.user_dto import UserRegistrationDTO, UserUpdatePasswordDTO, DeleteUserDTO


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
    
    async def update_password(self, updatepassword_dto: UserUpdatePasswordDTO)-> None:
        updatepassword_dto.new_password = updatepassword_dto.new_password + "_hashed"
        updatepassword_dto.current_password = updatepassword_dto.current_password + "_hashed"
        await self.user_repository.update_password(updatepassword_dto)

    async def delete_user(self, deleteuser_dto: DeleteUserDTO) -> None:
        deleteuser_dto.password = deleteuser_dto.password + "_hashed"
        await self.user_repository.delete_user(deleteuser_dto)



        