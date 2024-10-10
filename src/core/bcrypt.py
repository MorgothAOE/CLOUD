
# importo bcrypt
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def init_app(app):
    """
    inicializo bcrypt de acuerdo a la explicacion del 22/9
    dado que podria hacerlo en controllers, pero dada la explicacion y
    la documentacion se inicia aca.
    """
    bcrypt.init_app(app)
