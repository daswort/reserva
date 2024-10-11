from typing import Optional, Dict, Any
from fastapi import HTTPException, status

from app.core.exceptions.base_exceptions import AppBaseException

class InternalServerError(AppBaseException):
    """Excepción para un internal server error (500)."""
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    ERROR_CODE = "INTERNAL_SERVER_ERROR"
    MESSAGE = "Internal server error."

    def __init__(self, detail: Optional[str] = "Resource has a conflict"):
        super().__init__(
            status_code=self.STATUS_CODE,
            error_code=self.ERROR_CODE,
            message=self.MESSAGE,
            detail=detail
        )

class ConfilctError(AppBaseException):
    """Excepción para un recurso en conflicto (409)."""

    def __init__(self, detail: Optional[str] = "Resource has a conflict"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            error_code="CONFLICT",
            message="The requested resource has a conflict.",
            detail=detail
        )

class NotFoundError(AppBaseException):
    """Excepción para un recurso no encontrado (404)."""
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    ERROR_CODE = "NOT_FOUND"
    MESSAGE = "The requested resource could not be found."

    def __init__(self, detail: Optional[str] = "Resource not found"):
        super().__init__(
            status_code=self.STATUS_CODE,
            error_code=self.ERROR_CODE,
            message=self.MESSAGE,
            detail=detail
        )

class BadRequestError(AppBaseException):
    """Excepción para solicitudes incorrectas (400)."""
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Bad request"

class UnauthorizedError(AppBaseException):
    """Excepción para errores de autenticación (401)."""
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    ERROR_CODE = "UNAUTHORIZED"
    MESSAGE = "Unauthorized access to the resource."

    def __init__(self, detail: Optional[str] = "Unauthorized access"):
        super().__init__(
            status_code=self.STATUS_CODE,
            error_code=self.ERROR_CODE,
            message=self.MESSAGE,
            detail=detail
        )

