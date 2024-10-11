from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, Any, List

class RoleBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    
class RoleCreate(RoleBase):
    name: str
    description: str

class RoleUpdate(RoleBase):
    name: Optional[str] = None
    description: Optional[str] = None

class RoleInDB(RoleBase):
    id: int
    
    class Config:
        from_attributes = True 

class RoleOut(RoleInDB):
    name: Optional[str] = None
    description: Optional[str] = None