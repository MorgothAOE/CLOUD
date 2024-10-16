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

def assign_provider(provider, orden):
    orden.provider_id.append(provider)
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
        if order.entregado:
            return None 
        order.entregado = True
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

