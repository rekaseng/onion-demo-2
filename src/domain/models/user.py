from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    hashed_password: str

class UpdatePassword(BaseModel):
    email: str
    current_password: str
    new_password: str

class DeleteUser(BaseModel):
    email: str
    hashed_password: str


