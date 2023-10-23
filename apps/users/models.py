from typing import Optional, Union
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    id: int
    email: EmailStr
    password: str
    banned: bool = False
    ban_reason: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]


class CreateUserModel(BaseModel):
    email: EmailStr
    password: str


class UpdateUserModel(BaseModel):
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None
    banned: bool = False
    ban_reason: Optional[str] = None


class RetrieveUserModel(BaseModel):
    id: int
    email: EmailStr
    banned: bool
    ban_reason: Optional[str]
    updated_at: Optional[datetime]
    created_at: datetime
