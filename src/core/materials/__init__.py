from src.core.database import db
from src.core.materials.material import Material


def list_providers():
    """ DATOS DEL EJEMPLO """
    return Material.query.all()

def create_materials(**kwargs):
    """
    funcion para crear un usuario cuyos datos son pasados todos en kwargs
    tambien hashea la password
    """
    material = Material(**kwargs)
    db.session.add(material)
    db.session.commit()

    return material


def get_material_by_id(material_id):
    """
    Función que obtiene un material por su id (único).
    """
    return Material.query.filter_by(id=material_id).first()
