
from src.web.controllers.order import order_blueprint
from src.web.api.api_order import api_order_blueprint
from flask_swagger_ui import get_swaggerui_blueprint


def register(app):
   # UNA VEZ IMPORTADO, SE REGISTRA EN LA APP
   # CON ESTO SE AGREGA TODAS LAS RUTAS DEL BP A LA APP
   #controladores
   app.register_blueprint(order_blueprint)

    # API JSON
   app.register_blueprint(api_order_blueprint)


   SWAGGER_URL="/swagger"
   API_URL="/static/swagger.json"
   swagger_ui_blueprint = get_swaggerui_blueprint(
      SWAGGER_URL,
      API_URL,
      config={
         'app_name': 'Access API'
      }
   )
   app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)