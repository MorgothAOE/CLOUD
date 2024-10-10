from itsdangerous import URLSafeTimedSerializer

from src.web import config


def generate_token(email):
    """
    funcion que genera el token a partir de la secret key
    y la password salt definidas en config.py
    """
    serializer = URLSafeTimedSerializer(config.Config.SECRET_KEY)
    return serializer.dumps(email, salt=config.Config.SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    """
    funcion que parsea el token recibido como parametro
    """
    serializer = URLSafeTimedSerializer(config.Config.SECRET_KEY)
    try:
        email = serializer.loads(
            token, salt=config.Config.SECURITY_PASSWORD_SALT, 
            max_age=expiration
        )
        return email
    except Exception:
        return False
