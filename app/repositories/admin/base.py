from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession


# Definir tipos genéricos
ModelType = TypeVar("ModelType")
PrimaryKeyType = TypeVar("PrimaryKeyType", bound=Any)

class BaseRepository(ABC, Generic[ModelType, PrimaryKeyType]):
    def __init__(self, model: Type[ModelType]):
        """
        Inicializa el repositorio con el modelo de SQLAlchemy
        :param model: Modelo de SQLAlchemy
        """
        self.model = model

    @abstractmethod
    async def get(self, session: AsyncSession, id: PrimaryKeyType) -> Optional[ModelType]:
        """
        Recupera un registro por su ID.
        """
        pass

    @abstractmethod
    async def get_all(self, session: AsyncSession, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Recupera todos los registros, con paginación opcional.
        """
        pass

    @abstractmethod
    async def create(self, session: AsyncSession, obj_in: ModelType) -> ModelType:
        """
        Crea un nuevo registro en la base de datos.
        """
        pass

    @abstractmethod
    async def update(self, session: AsyncSession, db_obj: ModelType, obj_in: dict) -> ModelType:
        """
        Actualiza un registro existente con los datos proporcionados.
        """
        pass

    @abstractmethod
    async def delete(self, session: AsyncSession, id: PrimaryKeyType) -> None:
        """
        Elimina un registro por su ID.
        """
        pass
