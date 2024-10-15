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

api_order_blueprint = Blueprint("api_order", __name__, url_prefix="/api")
"""
Agrego un blueprint nuevo para manejar ordenes.
uso el prefijo /order para todo el controlador
"""

"""OLD APP IMPLEMENTATION"""
@api_order_blueprint.post("/login")
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
        return {"error": "Parámetros inválidos"}, 400
    if (api_mail_parse(email)):
        return {"error": "Parámetros inválidos"}, 400
    user = providers.check_provider(email, password)
    if not user:
        return {"error": "No existe el  usuario"}, 400
    
    resp = jsonify({'login': True})
    access_token = create_access_token(identity={"email": email})
    set_access_cookies(resp, access_token)
    return resp, 200


@api_order_blueprint.route('/logout', methods=['POST'])
def logoutfront():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200

@api_order_blueprint.get("/test")
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


@api_order_blueprint.post("/front-google-login")
def frontLoginGoogle():
    """
    api que recibe un 'authorization_token' del front, se lo envia a google
    para corroborar la identidad y en caso de ser correcto y
    estar registrado en la plataforma lo autentica y devuelve un token jwt
    """
    data_request = request.get_json()
    if 'code' in data_request:
        token_acceso = data_request['code']
        personDataUrl = "https://www.googleapis.com/userinfo/v2/me"
        personData = requests.get(personDataUrl, headers={
            "Authorization": f"Bearer {token_acceso}"
        }).json()
        if "email" in personData:
            user = providers.find_user_by_email(personData['email'])
            if user:
                access_token = create_access_token(
                    identity={"email": personData['email']})
                return {"token": access_token}, 200
            else:
                return {"error": "Email no registrado"}, 400
        else:
            return {"error": "Fallo la validacion del token con google"}, 400
    else:
        return {"error": "Parámetros inválidos"}, 400
