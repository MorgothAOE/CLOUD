from src.core.database import db
from src.core.providers.provider import MaterialProvider, Provider
from src.core.bcrypt import bcrypt


def list_providers():
    """ DATOS DEL EJEMPLO """
    return Provider.query.all()

def create_provider(**kwargs):
    """
    funcion para crear un usuario cuyos datos son pasados todos en kwargs
    tambien hashea la password
    """    
    hash = bcrypt.generate_password_hash(kwargs["password"].encode('utf-8'))
    kwargs.update(password=hash.decode('utf-8'))
    provider = Provider(**kwargs)
    db.session.add(provider)
    db.session.commit()

    return provider

def find_user_by_email(email):
    """
    funcion que me devuelve el usuario
    con el email pasado por parametro
    devuelve nada si no existe
    """
    return Provider.query.filter_by(email=email).first()

def check_provider(email, password):
    """
    funcion que me devuelve un usuario si el email
    y la contraseña son validos, 
    si alguno falla devuelve none
    """
    user = find_user_by_email(email)
    if user and check_password(user, password):
        return user
    else:
        return None
  
    
def check_password(user, password):
    """
    funcion que comprueba 2 contraseñas
    una plana y la otra correspondiendo al 
    usuario pasado como parametro    
    """
    return bcrypt.check_password_hash(user.password, password.encode('utf-8'))


def get_all_material_providers():
    """
    Devuelve una lista de todas las relaciones de MaterialProvider.
    """
    return MaterialProvider.query.all()


def get_materials_by_provider(provider_id):
    """
    Devuelve una lista de todos los materiales que provee un proveedor dado su ID.
    """
    return MaterialProvider.query.filter_by(provider_id=provider_id).all()


def get_providers_by_material(material_id):
    """
    Devuelve una lista de todos los proveedores que proveen un material dado su ID.
    """
    return MaterialProvider.query.filter_by(material_id=material_id).all()


def get_material_provider(provider_id, material_id):
    """
    Devuelve la relación MaterialProvider entre un proveedor y un material específicos.
    """
    return MaterialProvider.query.filter_by(provider_id=provider_id, material_id=material_id).first()


def add_for_material(**kwargs):
    """
    Esta función registra a un proveedor para cierto material.
    """

    mp = MaterialProvider(**kwargs)
    db.session.add(mp)
    db.session.commit()

def check_if_added(provider_id, material_id):
    return MaterialProvider.query.filter_by(provider_id=provider_id, material_id=material_id).first()