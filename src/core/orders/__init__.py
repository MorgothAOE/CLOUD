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