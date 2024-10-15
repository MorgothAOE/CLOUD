from functools import wraps
from flask import flash
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template

# SE IMPORTA DE CORE, LAS FUCNIONES NECESARIAS
# PARA HACER  LAS QUERYS EN LA BD
from src.core import board
from src.core import providers


import re


"""
    ESTA FUNCION ES PARA SABER SI UN USUARIOS ESTA LOGUEADO
    SE PUEDE UTILIZAR EN LOS TEMPLATES PARA AVERIGUAR SI EL
    USUARIOA QUE SE ESTA UTILIZANDO, ESTA LOGUEADO.
"""


def is_authenticated():
    """
    funcion que devuelve true si el hay un usuario
    autenticado, sino devuelve false
    """
    return session.get("user") is not None

"""
    Decorador: Encierra a la funcion que se quiere decorar
    -@wraps: Mantiene el contexto de la funcion decorada
    -decorated_function: Es la funcion que aplica la logica 
        que se quiere en el controlador
    -f(*args, **kwargs) es la funcion decorada o controlador
    -Se puede ejecutar codigo antes y despues de la funcion decorada

"""


def login_required(f):
    """
    funcion decoradora que utilizo para comprobar
    que el usuario esta autenticado
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            flash("Usted no tiene acceso a la url solicitada", "info")
            return redirect(url_for("home"))
        result = f(*args, **kwargs)
        return result
    return decorated_function

def api_mail_parse(email):
    """
    funcion que comprueba que el email recibido tenga forma de email
    """
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    errores = False
    # Parseo de datos

    # <- match me devuelve un string valido, por eso pregunto por "not string"
    if not re.match(pat, email):
        errores = True

# VERSION 1


def parse_email(email):
    """
    funcion que comprueba los datos de un usuario que se va a crear
    params es un diccionario que contiene los datos necesarios
    """
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    errores = False
    # Parseo de datos

    # <- match me devuelve un string valido, por eso pregunto por "not string"
    if not re.match(pat, email):
        errores = True
        flash(("Error al crear el usuario: El email "+
               "tiene un formato incorrecto"), "error")
    elif providers.find_user_by_email(email):
        errores = True
        flash("Error al crear el usuario: El email ya esta en uso", "error")
    return errores


