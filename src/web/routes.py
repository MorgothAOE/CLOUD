
from src.web.controllers.order import order_blueprint
from src.web.api.api_order import api_order_blueprint


def register(app):
   # UNA VEZ IMPORTADO, SE REGISTRA EN LA APP
   # CON ESTO SE AGREGA TODAS LAS RUTAS DEL BP A LA APP
   #controladores
   app.register_blueprint(order_blueprint)

    # API JSON
   app.register_blueprint(api_order_blueprint)
