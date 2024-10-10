# 1. Usa una imagen base de Python
FROM python:3.9-slim

# 2. Establece el directorio de trabajo en el contenedor
WORKDIR /src

# 3. Copia el archivo pyproject.toml y poetry.lock (si lo tienes)
COPY pyproject.toml poetry.lock* /src/

# 4. Instala Poetry
RUN pip install poetry

# 5. Instala las dependencias del proyecto sin crear el entorno virtual
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# 6. Copia todo el contenido del proyecto en el contenedor
COPY . /src

# 7. Exponer el puerto donde correrá la aplicación Flask
EXPOSE 5000

RUN docker-compose up -d

# 8. Definir el comando por defecto para correr la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
