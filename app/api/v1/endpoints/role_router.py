from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.admin.session import get_async_session
from app.services.admin.role_service import RoleService
from app.repositories.admin.role_repository import RoleRepository
from app.schemas.admin.role_schema import RoleCreate, RoleUpdate, RoleOut

router = APIRouter()

# Inyección de dependencias: Capa de servicio y repositorio
role_service = RoleService(RoleRepository())

# Crear rol
@router.post("/", response_model=RoleOut)
async def create_role(role_in: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    return await role_service.create_role(session, role_in)

# Obtener rol por ID
@router.get("/{role_id}", response_model=RoleOut)
async def get_role(role_id: int, session: AsyncSession = Depends(get_async_session)):
    return await role_service.get_role(session, role_id)

# Listar roles
@router.get("/", response_model=list[RoleOut])
async def list_roles(session: AsyncSession = Depends(get_async_session)):
    return await role_service.role_repo.get_multi(session)

# Actualizar rol
@router.put("/{role_id}", response_model=RoleOut)
async def update_role(role_id: int, role_in: RoleUpdate, session: AsyncSession = Depends(get_async_session)):
    return await role_service.update_role(session, role_id, role_in)

# Eliminar rol
@router.delete("/{role_id}")
async def delete_role(role_id: int, session: AsyncSession = Depends(get_async_session)):
    await role_service.delete_role(session, role_id)
    return {"message": "Role deleted successfully"}
