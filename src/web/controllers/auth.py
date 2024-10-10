from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from src.web.helpers.token import confirm_token
from src.web.helpers.token import generate_token
"""
from src.web.helpers.auth import user_register
from src.web.helpers.auth import login_required
from src.web.helpers.auth import is_authenticated
from src.web.helpers.auth import in_maintenance
"""
from authlib.integrations.flask_client import OAuth

from flask_jwt_extended import create_access_token
import requests

oauth = OAuth()


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
"""
Agrego un blueprint nuevo para manejar autenticacion.
uso el prefijo /auth para todo el controlador
"""


@auth_blueprint.get("/")
def login():
    """
    La ruta .../auth/ me deberia renderizar el formulario de login 
    """
    if session.get("user"):
        flash(("Usted ya inicio sesion en el sitio, si quiere iniciar" +
               " sesion con otra cuenta por favor cierre sesion."), "info")
        return redirect(url_for("home"))
    else:
        return render_template("auth/login.html")


@auth_blueprint.post("/authenticate")
def authenticate():
    """
    defino mi metodo para autenticar un usuario, la funcion es usada por 
    templates/auth/login.htm
    busca en la bd por un usuario con ese email y si el email y la contraseña
    son correctas inicia la sesion de ese usuario y lo lleva  a la pagina
    de inicio, caso contrario devuelve error
    """
    params = request.form

    user = auth.check_user(params["email"], params["password"])

    if not user:
        flash("Email o clave incorrecta.", "error")
        return redirect(url_for("auth.login"))

    return redirect(url_for("home"))


@auth_blueprint.get("/logout")
#@login_required
def logout():
    """
    Funcion que cierra la sesion del usuario
    """
    if session.get("user"):
        del session["user"]
        session.clear()
        flash("La sesion se ha cerrado correctamente.", "info")
    else:
        flash("no hay sesion iniciada.", "info")
    return redirect(url_for("home"))
