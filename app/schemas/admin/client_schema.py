from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, Any, List



class ClientBase(BaseModel):
    user_id: Optional[int] = None
    
class ClientCreate(ClientBase):
    user_id: int

class ClientUpdate(ClientBase):
    user_id: Optional[int] = None

class ClientInDB(ClientBase):
    id: int
    
    class Config:
        from_attributes = True 

class ClientOut(ClientInDB):
    user_id: Optional[int] = None
    user: Optional["UserOut"] = None

from app.schemas.admin.user_schema import UserOut