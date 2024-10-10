#from src.web.helpers import auth
"""
El archivo functions.py contiene las funciones que se 
registraran en la app, para utilizarlo  en jinja
"""


def register(app):
    """
    # FUNCION, PARA VERIFICAR SI EL USUARIO ESTA AUTENTICADO
    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)
    app.jinja_env.globals.update(is_enabled=auth.is_enabled)
    # app.jinja_env.globals.update(get_institutions=auth.get_institutions)
    # app.jinja_env.globals.update(has_access=auth.has_access)

    # FUNCION QUE DEVUELVE LA CONFIGURACION DEL SITIO PARA EL SUPERADMIN
    app.jinja_env.globals.update(get_configuration=auth.get_configuration)

    # FUNCION QUE DEVUELVE EL USUARIO ACTUAL
    app.jinja_env.globals.update(get_actual_user=auth.get_actual_user)
    """
