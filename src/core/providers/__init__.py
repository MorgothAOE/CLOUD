from src.core.database import db
from src.core.providers.provider import Provider
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


