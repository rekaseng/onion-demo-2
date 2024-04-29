from pydantic import BaseModel

class UserRegistrationDTO(BaseModel):
    username: str
    email: str
    password: str

class UserUpdatePasswordDTO(BaseModel):
    email: str
    current_password: str
    new_password: str

class DeleteUserDTO(BaseModel):
    email: str
    password: str

