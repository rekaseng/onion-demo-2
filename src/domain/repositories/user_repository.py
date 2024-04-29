from abc import ABC, abstractmethod
from typing import Optional, List
from domain.models.user import User, UpdatePassword, DeleteUser

class UserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_all(self) -> List[User]:
        pass

    @abstractmethod
    async def update_password(self, updatePassword:UpdatePassword) -> None:
        pass
    
    @abstractmethod
    async def delete_user(self, deleteUser:DeleteUser) -> None:
        pass