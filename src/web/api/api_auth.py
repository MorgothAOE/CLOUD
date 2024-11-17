from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from flask import jsonify
from src.core import orders
from src.core import providers
from src.web.schemas.order_schema import order_schema
from flask_cors import CORS
import requests
from src.web.helpers.auth import api_mail_parse

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

api_blueprint = Blueprint("api", __name__, url_prefix="/api")
"""
Agrego un blueprint nuevo para manejar ordenes.
uso el prefijo /order para todo el controlador
"""


@api_blueprint.post("/login")
def login():
    """
    api que se encarga de corroborar los datos y en caso de ser correctos
    autentica a un usuario y devuelve un token
    """
    data_request = request.get_json()
    if ('user' in data_request and 'password' in data_request):
        email = data_request['user']
        password = data_request['password']
    else:
        return {"error": "Credenciales Invalidas"}, 400
    if (api_mail_parse(email)):
        return {"error": "Credenciales Invalidas"}, 400
    user = providers.check_provider(email, password)
    if not user:
        return {"error": "Credenciales Invalidas"}, 400
    
    resp = jsonify({'login': True})
    access_token = create_access_token(identity={"email": email})
    set_access_cookies(resp, access_token)
    return resp, 200


@api_blueprint.route('/logout', methods=['POST'])
def logoutfront():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200

@api_blueprint.get("/test")
@jwt_required()
def test():
    """
    testea jwt nada mas
    """
    user = get_jwt_identity()
    if user:
        return 'sarasa', 200
    else:
        return 'no hay jwt creado',400



