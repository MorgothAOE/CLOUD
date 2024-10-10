from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from src.core import orders
from src.web.helpers.token import confirm_token
from src.web.helpers.token import generate_token
"""
from src.web.helpers.auth import user_register
from src.web.helpers.auth import login_required
from src.web.helpers.auth import is_authenticated
from src.web.helpers.auth import in_maintenance
"""
from authlib.integrations.flask_client import OAuth
from src.core import orders as order_core

from flask_jwt_extended import create_access_token
import requests

oauth = OAuth()

order_blueprint = Blueprint("auth", __name__, url_prefix="/order")
"""
Agrego un blueprint nuevo para manejar autenticacion.
uso el prefijo /auth para todo el controlador
"""

@order_blueprint.get("/")
def login():
    """
    La ruta .../auth/ me deberia renderizar el formulario de login 
    """
    orders = order_core.list_order()
    return render_template("order/index.html", orders=orders)
