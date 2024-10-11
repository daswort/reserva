from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from contextlib import asynccontextmanager
from app.core.config import settings as s

databse_url = f'postgresql+asyncpg://{s.TENANT_USER}:{s.TENANT_PASSWORD}@{s.POSTGRES_HOST}/{s.TENANT_NAME}'
s.set_variable("TENANT_DATABASE_URL", databse_url)

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