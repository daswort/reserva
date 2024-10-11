from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, Any, List

from app.schemas.admin.role_schema import RoleOut

class UserBase(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None
    role_id: Optional[int] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
    
class UserCreate(UserBase):
    full_name: str
    username: Optional[str] = None
    email: EmailStr
    hashed_password: str
    role_id: Optional[int] = None
    is_active: bool
    is_admin: bool

class UserUpdate(UserBase):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None 
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None

class UserInDB(UserBase):
    id: int
    
    class Config:
        from_attributes = True 

class UserOut(UserInDB):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None
    role_id: Optional[int] = None
    client_id: Optional[int] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
    created_at: Optional[datetime] = None
    role: Optional[RoleOut] = None
    client: Optional["ClientOut"] = None
    tenants: Optional[List[Any]] = []
    tasks: Optional[List[Any]] = []

from app.schemas.admin.client_schema import ClientOut