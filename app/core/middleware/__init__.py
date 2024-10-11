from fastapi import FastAPI
from app.core.middleware.cors import configure_cors
from app.core.middleware.logging_middleware import LogRequestMiddleware
from app.core.middleware.error_handling_middleware import ErrorHandlingMiddleware

def configure_middlewares(app: FastAPI) -> None:
    """
    Aplica todos los middlewares necesarios a la aplicación FastAPI.
    """
    app.add_middleware(LogRequestMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    
    # Configurar el middleware CORS
    configure_cors(app)