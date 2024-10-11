# app/services/admin/role_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.admin.role_repository import RoleRepository
from app.schemas.admin.role_schema import RoleCreate, RoleUpdate
from app.models.admin.role import Role
from fastapi import HTTPException

class RoleService:
    def __init__(self, role_repo: RoleRepository):
        self.role_repo = role_repo

    async def create_role(self, session: AsyncSession, role_in: RoleCreate) -> Role:
        existing_role = await self.role_repo.get_by_name(session, role_in.name)
        if existing_role:
            raise HTTPException(status_code=400, detail="Role already registered")
        
        new_role = Role(**role_in.model_dump())
        return await self.role_repo.create(session, new_role)

    async def get_role(self, session: AsyncSession, role_id: int) -> Role:
        role = await self.role_repo.get(session, role_id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    async def update_role(self, session: AsyncSession, role_id: int, role_in: RoleUpdate) -> Role:
        role = await self.get_role(session, role_id)
        updated_data = role_in.model_dump(exclude_unset=True)
        return await self.role_repo.update(session, role, updated_data)

    async def delete_role(self, session: AsyncSession, role_id: int) -> None:
        role = await self.get_role(session, role_id)
        await self.role_repo.delete(session, role.id)
