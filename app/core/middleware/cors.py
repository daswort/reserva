from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

def configure_cors(app: FastAPI) -> None:
    """
    Configura y aplica el middleware CORS a la aplicación FastAPI.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Permite todos los orígenes, cámbialo en producción.
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permite los métodos necesarios.
        allow_headers=["Authorization", "Content-Type"],  # Solo permite los headers necesarios.
    )