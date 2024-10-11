from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.admin.user import User
from app.repositories.admin.async_repository import AsyncRepository

class UserRepository(AsyncRepository):
    def __init__(self):
        super().__init__(User)

    async def get_by_email(self, session: AsyncSession, email: str) -> User:
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        return result.scalars().first()
    
