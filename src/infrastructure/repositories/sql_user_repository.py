from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from infrastructure.orm.user_orm_model import UserOrmModel

class SQLUserRepository(UserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_all(self)-> List[User]:
        result = await self.db_session.execute(select(UserOrmModel))
        orm_users = result.scalars().all()
        users = [item.to_domain() for item in orm_users]
        return users

    async def add(self, user: User) -> None:
        orm_user = UserOrmModel.from_domain(user)
        await self.db_session.merge(orm_user)
        await self.db_session.commit()

    async def get_by_email(self, email: str) -> User:
        result = await self.db_session.execute(select(UserOrmModel).filter(UserOrmModel.email == email))
        orm_user = result.scalars().first()

        if orm_user is None:
            return None

        user = orm_user.to_domain()
        return user
    
    async def update_user(self, email: str, password: str) -> None:
        # Check if the user exists
        result = await self.db_session.execute(select(UserOrmModel).filter_by(email=email))
        orm_user = result.scalars().first()

        if orm_user is None:
            return None

        # Update the user's password
        orm_user.hashed_password = password
        await self.db_session.commit()
    
    async def delete_user(self, email: str) -> None:
        # Check if the user exists and the password is correct
        result = await self.db_session.execute(select(UserOrmModel).filter_by(email=email))
        orm_user = result.scalars().first()
        if orm_user is None:
            return None
        
        # Delete the user
        await self.db_session.delete(orm_user)
        await self.db_session.commit()


        





