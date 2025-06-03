from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    """
    Schema for user creation request
    """
    email: constr(pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str

class UserLogin(BaseModel):
    """
    Schema for user login request
    """
    email: constr(pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str

class UserResponse(BaseModel):
    """
    Schema for user response
    """
    id: str
    email: EmailStr
    created_at: datetime
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None

    class Config:
        from_attributes = True 