# app/core/logging_config.py
from loguru import logger
import sys
import os

# Configuración básica
logger.remove()  # Elimina los handlers por defecto
logger.add(
    sys.stdout, 
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    backtrace=True, 
    diagnose=True
)  # Logs a consola

# Ruta para guardar los archivos de logs
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Logs a un archivo, rotación diaria y compresión
logger.add(
    f"{log_dir}/app_log_{{time}}.log", 
    rotation="00:00",  # Rotación diaria
    retention="7 days",  # Retener archivos por 7 días
    compression="zip",  # Comprimir los logs
    level="DEBUG", 
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {file}:{line}"
)

# Ejemplo de cómo utilizar en otros módulos
logger.info("Logging system initialized!")
