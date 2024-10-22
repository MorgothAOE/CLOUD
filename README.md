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

## Datos cargados
- En el archivo ubicado en src/core/board de nombre 'seeds.py' se especifican los datos cargados en la base de datos para realizar las pruebas
- Hay 4 materiales de los que se puede ser proveedor: Hierro, carton, aluminio y plastico
- El deposito Tolosa (tolosa@gmail.com) tiene 2 ordenes, 1 solo esta reservada y la otra ya fue entregada. Maneja aluminio y plastico
- El deposito Los Hornos (lhornos@gmail.com) tiene 2 ordenes las cuales solos estan reservadas, faltaria entregarlas. Maneja carton y Hierro
- El deposito Parque Saavedra (saavedra@gmail.com) No tiene ni materiales asignados ni ordenes reservadas y/o entregadas.