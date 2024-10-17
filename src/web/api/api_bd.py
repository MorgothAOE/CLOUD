from flask import Blueprint
from flask import make_response
from flask import jsonify

from src.web.api.api_auth import api_blueprint
from src.core import database
from src.core.board import seeds

# Estos endpoints son para configurar la BD de producción.

bd_blueprint = Blueprint("bd", __name__, url_prefix="/bd")


@api_blueprint.post("/reset-db")
def reset_db():
    try:
        database.reset_db()
        return make_response(jsonify({"message": "Database reset successful"}), 200)
    except Exception as e:
        # Registrar el error para poder revisar qué falló
        print(f"Error reseteando la base de datos: {str(e)}")
        return make_response(jsonify({"error": "Database reset failed"}), 400)


@api_blueprint.post("/seeds-db")
def seeds_db():
    try:
        seeds.run()
        return make_response(jsonify({"message": "Seeding database successful"}), 200)
    except Exception as e:
        # Registrar el error para revisión
        print(f"Error en la carga inicial de datos: {str(e)}")
        return make_response(jsonify({"error": "Database seeding failed"}), 400)
