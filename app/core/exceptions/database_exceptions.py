from typing import Optional, Dict
from app.core.exceptions.base_exceptions import AppBaseException

class DatabaseConnectionError(AppBaseException):
    """Error de conexión a la base de datos."""
    def __init__(self, detail: Optional[str] = "A database connection error occurred."):
        super().__init__(
            status_code=500,
            error_code="DB_CONNECTION_ERROR",
            message="Failed to connect to the database.",
            detail=detail
        )

class IntegrityError(AppBaseException):
    """Error de integridad de la base de datos."""
    def __init__(self, detail: Optional[str] = "Database integrity violation"):
        super().__init__(
            status_code=500,
            error_code="DB_INTEGRITY_ERROR",
            message="A database integrity error occurred.",
            detail=detail
        )

class RecordNotFoundError(AppBaseException):
    """Excepción para cuando un registro no se encuentra en la base de datos."""
    def __init__(self, detail: Optional[str] = "Record not found in the database."):
        super().__init__(
            status_code=500,
            error_code="DB_NOT_FOUND_ERROR",
            message="The requested resource could not be found.",
            detail=detail
        )
