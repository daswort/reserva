# app/services/admin/user_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.admin.user_repository import UserRepository
from app.schemas.admin.user_schema import UserCreate, UserUpdate
from app.models.admin.user import User
from fastapi import status
from app.core.exceptions.repository_exceptions import CreateError
from app.core.exceptions.http_exceptions import ConfilctError, InternalServerError, NotFoundError

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, session: AsyncSession, user_in: UserCreate) -> User:
        try:
            existing_user = await self.user_repo.get_by_email(session, user_in.email)
            if existing_user:
                raise ConfilctError(detail="Email already registered")
        
            new_user = User(**user_in.model_dump())
            return await self.user_repo.create(session, new_user, load_relations=["role", "client"])
        except CreateError as e:
            raise InternalServerError(detail=e.message)



    async def get_user(self, session: AsyncSession, user_id: int) -> User:
        user = await self.user_repo.get(session, user_id, load_relations=["role", "client"])
        if not user:
            raise NotFoundError(detail="User not found")
        return user

    async def update_user(self, session: AsyncSession, user_id: int, user_in: UserUpdate) -> User:
        user = await self.get_user(session, user_id)
        updated_data = user_in.model_dump(exclude_unset=True)
        return await self.user_repo.update(session, user, updated_data)

    async def delete_user(self, session: AsyncSession, user_id: int) -> None:
        user = await self.get_user(session, user_id)
        await self.user_repo.delete(session, user.id)
