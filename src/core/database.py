from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """
        Inicializacion de la aplicacion
    """

    db.init_app(app)
    config_db(app)


def config_db(app):
    """
        Configuracion de la aplicacion
    """
    @app.teardown_request
    def close_session(exception=None):
        """
            Cierra la sesion de la base de datos
        """
        db.session.close()


def reset_db():
    """
        Reinicia la base de datos
    """
    print("Eliminando BD...")
    db.drop_all()
    print("Creando BD...")
    db.create_all()
