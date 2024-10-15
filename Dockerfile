# 1. Usa una imagen base de Python
FROM python:3.10

# 2. Establece el directorio de trabajo en el contenedor
WORKDIR ./project

# 6. Copia todo el contenido del proyecto en el contenedor
COPY . /project

# 4. Instala Poetry
RUN pip install poetry

# 5. Instala las dependencias del proyecto sin crear el entorno virtual
RUN poetry install

# 7. Exponer el puerto donde correrá la aplicación Flask
EXPOSE 5000

#RUN docker-compose up -d

#RUN flask resetdb

#RUN flask seedsdb

# 8. Definir el comando por defecto para correr la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
