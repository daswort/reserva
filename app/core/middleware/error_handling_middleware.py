from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.exceptions.base_exceptions import AppBaseException
from app.core.config import settings as s
from loguru import logger

class ErrorHandlingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except RequestValidationError as e:
            print('ERRORSSS', e.errors())

        except AppBaseException as e:
            # Manejo de excepciones específicas de la aplicación
            logger.error(f"Application error: {str(e)}")
            return JSONResponse(content=e.error_response.model_dump(), status_code=e.error_response.status_code)        
        
        except Exception as e:
            # Mostrar más detalles en entornos de desarrollo
            if s.ENV == "development":
                # Capturar y mostrar el backtrace completo
                logger.opt(exception=True).error(f"Unhandled exception: {str(e)}")
            else:
                # No mostrar detalles en producción
                logger.error(f"Unhandled exception: {str(e)}")
            
            return JSONResponse(
                content={
                    "status_code": 500, 
                    "error_code": "INTERNAL_SERVER_ERROR", 
                    "message": "Internal server error", 
                    "detail": str(e)
                },
                status_code=500
            )
