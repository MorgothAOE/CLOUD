from datetime import datetime
from src.core.materials.material import Material
from src.core.database import db
from src.core.orders.order import Order


def list_order():
    """ DATOS DEL EJEMPLO """
    return Order.query.all()

def create_order(**kwargs):
    """
    funcion para crear un usuario cuyos datos son pasados todos en kwargs
    tambien hashea la password
    """
    order = Order(**kwargs)
    db.session.add(order)
    db.session.commit()

    return order

def reserve_order(provider, orden):
    orden.provider_id.append(provider)
    orden.reserved_at = datetime.utcnow()
    db.session.add(orden)
    db.session.commit()
    return orden

def assign_material(material, orden):
    orden.material_id.append(material)
    db.session.add(orden)
    db.session.commit()
    return orden

def mark_order_as_delivered(order_id):
    """
    Marca una orden como entregada (entregado=True) solo si no ha sido entregada ya.
    """
    order = Order.query.get(order_id)
    if order:
        if order.delivered_at:
            return None 
        order.delivered_at = datetime.utcnow()
        db.session.commit()
        return order
    else:
        return None 
    

def get_order(order_id):
    """
    Devuelve los detalles de una orden específica.
    """
    order = Order.query.get(order_id)
    if order:
        return order
    else:
        return None 

def get_orders_by_material_id(material_id):
    """
    Devuelve todas las órdenes relacionadas con un material específico por su id.
    """
    orders = Order.query.filter_by(material_id=material_id).all()
    return orders


def get_orders_by_material_name(material_name):
    """
    Devuelve todas las órdenes relacionadas con un material específico por su nombre.
    """
    material = Material.query.filter_by(nombre=material_name).first()
    if material:
        orders = Order.query.filter_by(material_id=material.id).all()
        return orders
    else:
        return None 


