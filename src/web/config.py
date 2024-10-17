# MODULO DE PYTHON PARA LEVANTAR VARIABLES DE ENTORNO
import os



class Config(object):
    """Base  configuration"""
    SECURITY_PASSWORD_SALT = "muchasarasa"
    SECRET_KEY = "excesodesarasa"
    TESTING = False
    SESSION_TYPE = "filesystem"
    JSON_SORT_KEYS = False

    # Mail Settings
    # Defino mis configuraciones para el uso de flask-mail
    # que utilizo para enviar un email de confirmacion
    MAIL_DEFAULT_SENDER = "noreply@flask.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = 'noreplypdsgrupo02@gmail.com'
    MAIL_PASSWORD = 'ydaz qckt ulii jdle'

# HEREDA DE CONFIG


class ProductionConfig(Config):
    """
        Production configuration.
        SE SETEA LOS VALORES DE LA DB CON VARIABLES DE ENTORNO
        YA QUE EN PRODUCCION, NO SE TIENE LOS MISMOS VALORES QUE EN DESARROLLO
    """

    # EN PRODUCCION, LAS VARIABLES DE ENTORNO,
    # SE LLAMAN IGUAL QUE LAS VARIABLES UTILIZADAS
    #DB_USER = "pgadmin"
    #DB_PASS = "changeme"
    #DB_HOST = "10.103.0.2"
    #DB_NAME = "postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Development configuration."""

    # MODIFIQUENLO, CON LOS VALORES DE SU BD
    DB_USER = "pgadmin"
    DB_PASS = "changeme"
    DB_HOST = "127.0.0.1"
    DB_NAME = "postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True


"""
    # SE DEFINE UN DICCIONAROI, QUE DE ACUERDO A LA CLAVE, 
        ELIGUE ALGUNA DE LAS 3 CLASES
    # ES IMPORTANTE QUE LAS CLAVES SE RESPETEN
    # ESTE DICCIONARIO SE UTILIZA EN EL INIT DE LA APLICACION, 
        PARA SELECCIONAR CON QUE AMBIENTE TRABAJAR
"""
config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig
}
