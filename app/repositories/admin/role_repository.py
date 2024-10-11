from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.admin.role import Role
from app.repositories.admin.async_repository import AsyncRepository

class RoleRepository(AsyncRepository):
    def __init__(self):
        super().__init__(Role)

    async def get_by_name(self, session: AsyncSession, name: str) -> Role:
        query = select(Role).where(Role.name == name)
        result = await session.execute(query)
        return result.scalars().first()

