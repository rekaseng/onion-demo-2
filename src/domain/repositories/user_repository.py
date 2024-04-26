from abc import ABC, abstractmethod
from typing import Optional, List
from domain.models.user import User

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
    async def update_user(self, email: str, new_password:str) -> None:
        pass
    
    @abstractmethod
    async def delete_user(self, email: str) -> None:
        pass