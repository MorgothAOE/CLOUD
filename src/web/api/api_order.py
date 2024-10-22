from src.core.providers.provider import MaterialProvider
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from flask import jsonify
from flask import make_response
from src.core import orders
from src.core.orders import Order
from src.core import providers
from src.core import materials
from src.web.schemas.order_schema import order_schema
from flask_cors import CORS
from flask import request, jsonify
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import set_refresh_cookies
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies


order_blueprint = Blueprint("order", __name__, url_prefix="/api/order")
"""
Agrego un blueprint nuevo para manejar ordenes.
uso el prefijo /order para todo el controlador
"""


@order_blueprint.get("/list")
@jwt_required()
def list_orders():
    """
    Filtra órdenes basadas en material_id, material_name, rango de fechas (inserted_at),
    y si las órdenes no están reservadas y aún están disponibles.
    """
    material_id = request.args.get("material_id")
    material_name = request.args.get("material_name")
    start_date = request.args.get("start_date")  # Formato esperado: "YYYY-MM-DD"
    end_date = request.args.get("end_date")      # Formato esperado: "YYYY-MM-DD"
    only_unreserved = request.args.get("only_unreserved", type=bool, default=False)  # Filtrar solo las no reservadas

    filtered_orders = []

    if material_id:
        filtered_orders = orders.get_orders_by_material_id(material_id)
    elif material_name:
        filtered_orders = orders.get_orders_by_material_name(material_name)
    else:
        filtered_orders = orders.list_order()

    if start_date and end_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        filtered_orders = [order for order in filtered_orders if start_date <= order.available_until <= end_date]

    if only_unreserved:
        filtered_orders = [
            order for order in filtered_orders
            if order.reserved is False and order.available_until > datetime.utcnow()
        ]

    orders_data = [order.to_dict() for order in filtered_orders]

    if orders_data:
        return jsonify(orders_data), 200
    else:
        return jsonify({"error": "No se encontraron órdenes con los filtros proporcionados"}), 404



@order_blueprint.put("/<int:order_id>/delivered")
@jwt_required()
def mark_order_as_delivered(order_id):
    """
    Marca una orden como entregada si no lo está ya.
    """
    current_user = get_jwt_identity()
    email = current_user.get("email")

    provider = providers.find_user_by_email(email)
    order = orders.get_order(order_id)
    if not provider or order.provider_id != provider.id:
        return {"error": "No tienes permisos para entregar la orden"}, 403
    if not order.reserved_at:
        return {"error": "No se puede entregar una orden no reservada"}, 403
    
    order = orders.mark_order_as_delivered(order_id) 
    if order:
        return {"message": "La orden fue marcada como entregada correctamente"}, 200
    else:
        return {"error": "La orden no existe o ya fue entregada"}, 400
    


@order_blueprint.post("/<int:order_id>/reserve")
@jwt_required()
def reserve_order(order_id):
    """
    Asigna un proveedor a una orden si no ha sido reservada ya y verifica que el proveedor
    esté registrado como proveedor del material asociado a la orden.
    """
    current_user = get_jwt_identity()
    email = current_user.get("email")

    provider = providers.find_user_by_email(email)

    if not provider:
        return {"error": "No tienes permisos para reservar la orden"}, 403

    order = orders.get_order(order_id)

    if not order:
        return {"error": "La orden no existe"}, 404

    if order.reserved == True:
        return {"error": "La orden ya ha sido reservada"}, 400
    
    if order.available_until != None and order.available_until < datetime.utcnow():
        return {"error": "La orden ya no se encuentra disponible"}, 400

    # Verificar si el proveedor está registrado para el material de la orden
    material_provider = providers.get_material_provider(provider.id, order.material_id)
    if not material_provider:
        return {"error": f"El proveedor {provider.nombre_deposito} no está registrado para este material"}, 403

    # Asignar el proveedor y actualizar la fecha de reserva
    orders.reserve_order(provider, order)

    return {
        "message": f"La orden {order_id} fue reservada correctamente por el proveedor {provider.nombre_deposito}"
    }, 200


@order_blueprint.post("/material/register/<int:material_id>")
@jwt_required()
def register_provider_for_material(material_id):
    """
    Se recibe el endpoint del material y se registra al proveedor
    que llama para ese material.
    """

    current_user = get_jwt_identity()

    provider = providers.find_user_by_email(current_user.get('email'))

    if not provider:
        return make_response(jsonify({'error': 'No tienes permisos para reservar la orden'}), 403)

    material = materials.get_material_by_id(material_id)

    if not material:
        return make_response(jsonify({'error': 'No se encontró el material'}), 404)

    providers.add_for_material(
        provider_id=provider.id,
        material_id=material_id
    )

    return make_response(jsonify({
        'message': f'Se registró correctamente al proveedor {provider.nombre_deposito} para el material {material.nombre}'}), 201)



@order_blueprint.get("/myorders")
@jwt_required()
def list_orders_by_material():
    """
    Lista las órdenes de un provedor, puede filtrar por reservadas, entregadas o todas.
    """
    current_user = get_jwt_identity()
    provider = providers.find_user_by_email(current_user.get('email'))
    
    status = request.args.get("status")

    filtered_orders = []
    filtered_orders = orders.get_orders_by_provider_id(provider.id)

    if(status):
        if(status=='reserved'):
            filtered_orders = [order for order in filtered_orders if order.delivered == False]    
        elif(status=='delivered'):
            filtered_orders = [order for order in filtered_orders if order.delivered == True]   
        
    orders_data = [order.to_dict() for order in filtered_orders]

    if orders_data:
        return jsonify(orders_data), 200
    else:
        return jsonify({"error": "No se encontraron órdenes a cargo suyo"}), 404

@order_blueprint.get("/material_list")
@jwt_required()
def list_materials():
        
    filtered_materials = materials.list_materials()
    material_data = [material.to_dict() for material in filtered_materials]

    if material_data:
        return jsonify(material_data), 200
    else:
        return jsonify({"error": "No hay materiales cargados"}), 404