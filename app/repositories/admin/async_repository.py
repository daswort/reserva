from typing import Any, TypeVar, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from app.core.exceptions.repository_exceptions import CreateError
from loguru import logger

from app.repositories.admin.base import BaseRepository

ModelType = TypeVar("ModelType")
PrimaryKeyType = TypeVar("PrimaryKeyType", bound=Any)


class AsyncRepository(BaseRepository[ModelType, PrimaryKeyType]):
    async def get(
        self, 
        session: AsyncSession, 
        id: PrimaryKeyType,
        load_relations: Optional[List[str]] = None
    ) -> Optional[ModelType]:
        """
        Recupera un registro por su ID con la opción de cargar relaciones específicas.
        """
        try:
            if not load_relations:
                return await session.get(self.model, id)
            
            query = select(self.model).filter_by(id=id)

            options = [selectinload(getattr(self.model, relation)) for relation in load_relations]
            query = query.options(*options)

            result = await session.execute(query)
            obj_with_relations = result.scalars().first()

            return obj_with_relations
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener el registro: {str(e)}")

    async def get_all(self, session: AsyncSession, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Recupera todos los registros con paginación.
        """
        try:
            result = await session.execute(select(self.model).offset(skip).limit(limit))
            return result.scalars().all()
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener los registros: {str(e)}")
        
    async def create(
        self, 
        session: AsyncSession, 
        obj_in: ModelType, 
        load_relations: Optional[List[str]] = None
    ) -> ModelType:
        """
        Crea un nuevo registro en la base de datos, con la opción de cargar relaciones específicas.
        :param load_relations: Lista de relaciones a cargar (opcional).
        """
        try:
            session.add(obj_in)
            await session.commit()
            await session.refresh(obj_in)

            # Si hay relaciones que se quieren cargar, usamos selectinload para cargarlas
            if load_relations:
                return await self.get(session, obj_in.id, load_relations=load_relations)

            return await self.get(session, obj_in.id)

        except SQLAlchemyError as e:
            await session.rollback()
            logger.error(f"Database error during creation: {str(e)}")
            raise CreateError(detail=str(e))

    async def update(self, session: AsyncSession, db_obj: ModelType, obj_in: dict) -> ModelType:
        """
        Actualiza un registro existente.
        """
        try:
            for field, value in obj_in.items():
                setattr(db_obj, field, value)
            await session.commit()
            await session.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Error al actualizar el registro: {str(e)}")

    async def delete(self, session: AsyncSession, id: PrimaryKeyType) -> None:
        """
        Elimina un registro por su ID.
        """
        try:
            obj = await session.get(self.model, id)
            if not obj:
                raise HTTPException(status_code=404, detail="Registro no encontrado")
            await session.delete(obj)
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Error al eliminar el registro: {str(e)}")
