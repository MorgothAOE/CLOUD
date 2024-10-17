# CLOUD

URL: https://cloud-fd43.onrender.com

## Variables de entorno
- En nuestro caso, manemos 2 variables de entorno.
  - `FLASK_ENV`: Para determinar el ambiente en el que estamos y cargar la configuración adecuada.
  - `DATABASE_URL` (solo en producción): Para determinar la URL para la interacción con la BD en el cloud.
- Para tener las variables de entorno en desarrollo (en local):
  - Crear un archivo llamado `.env` en el directorio del proyecto.
  - Linux:
    ```bash
    export FLASK_ENV=development
    ```
  - Windows 💩​:
    ```powershell
    set FLASK_ENV=development
    ```