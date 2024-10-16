from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from flask import jsonify
from src.core import orders
from src.core.orders import Order
from src.core import providers
from src.web.schemas.order_schema import order_schema
from flask_cors import CORS
import requests
from src.web.helpers.auth import api_mail_parse
from src.web.api.api_auth import api_blueprint

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies


order_blueprint = Blueprint("order", __name__, url_prefix="/order")
"""
Agrego un blueprint nuevo para manejar ordenes.
uso el prefijo /order para todo el controlador
"""

@api_blueprint.get()
@jwt_required()
def list_all_orders():
    """
    Lista todas las órdenes.
    """
    all_orders = orders.list_order() 
    orders_data = [order.to_dict() for order in all_orders]  
    return jsonify(orders_data), 200



@api_blueprint.get("/material/<int:material_id>")
@jwt_required()
def list_orders_by_material(material_id):
    """
    Lista las órdenes de un material específico por su ID.
    """
    material_orders = orders.get_orders_by_material_id(material_id)
    if material_orders:
        orders_data = [order.to_dict() for order in material_orders]
        return jsonify(orders_data), 200
    else:
        return {"error": "No se encontraron órdenes para el material especificado"}, 404



@api_blueprint.get("/material/name/<string:material_name>")
@jwt_required()
def list_orders_by_material_name(material_name):
    """
    Lista las órdenes de un material específico por su nombre.
    """
    material_orders = orders.get_orders_by_material_name(material_name)
    if orders:
        orders_data = [order.to_dict() for order in material_orders]
        return jsonify(orders_data), 200
    else:
        return {"error": "No se encontraron órdenes para el material especificado"}, 404



@api_blueprint.put("/<int:order_id>/delivered")
@jwt_required()
def mark_order_as_delivered(order_id):
    """
    Marca una orden como entregada si no lo está ya.
    """
    order = orders.mark_order_as_delivered(order_id) 
    if order:
        return {"message": "La orden fue marcada como entregada correctamente"}, 200
    else:
        return {"error": "La orden no existe o ya fue entregada"}, 400
    


@api_blueprint.post("/<int:order_id>/reserve")
@jwt_required()
def reserve_order(order_id):
    """
    Asigna un provider a una orden si no ha sido reservada ya.
    """
    current_user = get_jwt_identity()  
    email = current_user.get("email")  

    provider = providers.find_user_by_email(email)

    if not provider:
        return {"error": "No tienes permisos para reservar la orden"}, 403

    order = orders.get_order(order_id)

    if not order:
        return {"error": "La orden no existe"}, 404

    if order.provider_id != 0:
        return {"error": "La orden ya ha sido reservada"}, 400

    orders.assign_provider(provider, order)

    return {
        "message": f"La orden {order_id} fue reservada correctamente por el proveedor {provider.nombre_deposito}"
    }, 200
