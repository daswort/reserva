from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.admin.session import get_async_session
from app.services.admin.user_service import UserService
from app.repositories.admin.user_repository import UserRepository
from app.schemas.admin.user_schema import UserCreate, UserUpdate, UserOut

router = APIRouter()

# Inyección de dependencias: Capa de servicio y repositorio
user_service = UserService(UserRepository())

# Crear usuario
@router.post("/", response_model=UserOut)
async def create_user(user_in: UserCreate, session: AsyncSession = Depends(get_async_session)):
    return await user_service.create_user(session, user_in)

# Obtener usuario por ID
@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    return await user_service.get_user(session, user_id)

# Listar usuarios
@router.get("/", response_model=list[UserOut])
async def list_users(session: AsyncSession = Depends(get_async_session)):
    return await user_service.user_repo.get_multi(session)

# Actualizar usuario
@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user_in: UserUpdate, session: AsyncSession = Depends(get_async_session)):
    return await user_service.update_user(session, user_id, user_in)

# Eliminar usuario
@router.delete("/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    await user_service.delete_user(session, user_id)
    return {"message": "User deleted successfully"}
