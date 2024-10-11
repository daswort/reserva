import os
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, EmailStr, field_validator
from typing import List, Optional, Union
from decouple import config as env_config

class Settings(BaseSettings):
    # Configuración general
    ENV: str = "development"
    DEBUG: bool = False
    API_VERSION: str = "v1"

    # Configuración de la base de datos
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str

    ADMIN_DB_USER: str
    ADMIN_DB_PASSWORD: str
    ADMIN_DB_NAME: str
    ADMIN_DB_DATABASE_URL: str

    TENANT_USER: str
    TENANT_PASSWORD: str
    TENANT_NAME: str
    TENANT_DATABASE_URL: str

    # Seguridad
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Configuración de CORS
    ALLOWED_ORIGINS: str

    # Configuración de email (ejemplo)
    EMAIL_SERVER: Optional[str]
    EMAIL_PORT: Optional[int]
    EMAIL_USERNAME: Optional[EmailStr]
    EMAIL_PASSWORD: Optional[str]

    # Configuración de Redis (ejemplo)
    REDIS_URL: Optional[str]

    @field_validator("POSTGRES_HOST")
    def assemble_postgres_host(cls, v: str) -> str:
        is_docker = env_config('IS_DOCKER', default='False').lower() == 'true'
        if not is_docker:
            v = "localhost"
        return v

    @field_validator("ALLOWED_ORIGINS")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

    class Config:
        # Cargar variables desde un archivo .env
        env_file = ".env"
        env_file_encoding = "utf-8"

    def set_variable(self, key: str, value: str):
        """Función para cambiar dinámicamente una variable de entorno."""
        os.environ[key] = value
        # Recargar toda la configuración
        self.__dict__.update(self.__class__().__dict__)

settings = Settings()