from flask import Flask
from flask import render_template
# importo sesiones de flask
from flask_session import Session
# SE IMPORTA LOS CONTROLADORES DE ERROR
from src.web import error
# Importo las rutas
from src.web import routes
# SE IMPORTA LA BD
from src.core import database
# SE IMPORTA EL BOARD PARA POPULAR LA BD
from src.core.board import seeds
# SE IMPORTA EL DICCIONARIO, CON LAS POSIBLES CONFIGURACIONES DE ENTORNO
from src.web.config import config
# Importo las sesiones
from flask import session
# Importo las funciones a utilizar en jinja
from src.web import functions
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.web.controllers.auth import oauth
import os

session_app = Session()
"""
   PARAM 1: INDICA EL MODO DE EJECUCION DE LA APLICACION
"""


def create_app(static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)

    env = os.getenv('FLASK_ENV', 'development')

    # SON LAS CLAVES PARA QUE ANDE WTFORMS
    app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

    # SE CONFIGURA LA APLICACION A PARTIR DEL OBJETO RECIBIDO
    # Y ESTE OBJETO LE ENVIA LAS VARIABLES NECESARIAS
    app.config.from_object(config[env])

    # PRINT PARA VER LA CLASE DE CONFIG
    # print("CLASE")
    # print(config[env])

    # PRINT PARA VER LA CONFIGURACION DE LA APP
    # print(app.config)

    # inicio la sesison, el SESSION_TYPE esta en config.py
    session_app.init_app(app)

    # SE INICIALIZA LA BD
    database.init_app(app)

    # REGISTRO LAS FUNCIONES
    functions.register(app)

    routes.register(app)
    # OBTENGO SI EXISTE LA SESION

    @app.get("/")
    def home():
        return render_template("home.html", logged=False)

    app.register_error_handler(404, error.not_found_error)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seedsdb")
    def seedsdb():
        seeds.run()

    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = "muchoMAYORexcesoDEsaras"  # Change this!
    # Enable csrf double submit protection. See this for a thorough
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False #En true va a ser necesario pasar el csrf en swagger
    # explanation: http://www.redotheweb.com/2015/11/09/api-security.html
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_ACCESS_COOKIE_NAME'] = "access_token_cookie"
    #app.config["JWT_COOKIE_SECURE"] = True
    jwt = JWTManager(app)
    """
    CORS(app)
    #CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app, resources={r"/api/*": {"origins": [
        "http://localhost:5173/*",
        "http://127.0.0.1:5173/*",
        "https://admin-grupo02.proyecto2023.linti.unlp.edu.ar/*"]}}, supports_credentials = True)
    oauthdict = {
        "OAUTH2_CLIENT_ID": "92524443474-so7j78to0lqvjqvkkg99to3b0athl92p.apps.googleusercontent.com",
        "OAUTH2_CLIENT_SECRET": "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",
        "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
        "FLASK_SECRET": "excesodesarasa",
        "FLASK_PORT": 5000
    }

    oauth.register("FlaskApp",
                   client_id=oauthdict.get("OAUTH2_CLIENT_ID"),
                   client_secret=oauthdict.get("OAUTH2_CLIENT_SECRET"),
                   client_kwargs={
                       "scope": "openid profile email https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read",
                   },
                   server_metadata_url=f'{oauthdict.get("OAUTH2_META_URL")}',
                   )

    oauth.init_app(app)
    """
    return app
