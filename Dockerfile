# Usa la imagen oficial de Python 3.12 slim como base
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install poetry

# Copia los archivos de proyecto necesarios
COPY pyproject.toml poetry.lock ./

# Instala las dependencias del proyecto sin crear un entorno virtual adicional
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Copia todo el código fuente
COPY . .

# Expone el puerto de la aplicación
EXPOSE 8000

# Ejecuta la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]