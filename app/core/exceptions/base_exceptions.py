from typing import Optional, Dict
from fastapi import HTTPException
from app.core.exceptions.schemas import ErrorResponseModel

class AppBaseException(Exception):
    """Excepción base para todas las excepciones de la aplicación."""
    def __init__(
        self, 
        status_code: int, 
        error_code: str, 
        message: str, 
        detail: Optional[str] = None
    ):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        self.detail = detail

        self.error_response = ErrorResponseModel(
            status_code=self.status_code,
            error_code=self.error_code,
            message=self.message,
            detail=self.detail
        )

        #super().__init__(status_code=status_code, detail=self.error_response.model_dump_json())

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"


class CriticalAppError(AppBaseException):
    """Error crítico que requiere atención inmediata."""
    pass

class NonCriticalAppError(AppBaseException):
    """Error no crítico, que puede ser manejado sin detener la ejecución."""
    pass
