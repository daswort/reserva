from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from decouple import config as env_config
from contextlib import asynccontextmanager
from app.core.config import settings

databse_url = f'postgresql+asyncpg://{settings.ADMIN_DB_USER}:{settings.ADMIN_DB_PASSWORD}@{settings.POSTGRES_HOST}/{settings.ADMIN_DB_NAME}'
settings.set_variable("ADMIN_DB_DATABASE_URL", databse_url)

async def get_async_session():
    engine = create_async_engine(
        databse_url,
        echo=False,  # Cambiar a True para depuración
        future=True,
        pool_pre_ping=True,  # Verifica que la conexión sigue viva
        pool_size=10,  # Tamaño del pool de conexiones
        max_overflow=20,  # Conexiones adicionales si el pool está lleno
    )
    AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
    async with AsyncSessionLocal() as db:
        yield db