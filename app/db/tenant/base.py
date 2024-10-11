from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import inspect
from typing import Any

class Base(DeclarativeBase):
    id: Any
    __name__: str

    # Generar automáticamente __tablename__ en minúsculas
    @classmethod
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # Método para obtener las columnas clave primaria
    @classmethod
    def primary_key_columns(cls):
        return [key for key, col in inspect(cls).columns.items() if col.primary_key]
