from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    hashed_password: str