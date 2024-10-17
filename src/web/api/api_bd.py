from flask import Blueprint

from src.web.api.api_auth import api_blueprint
from src.core import database
from src.core.board import seeds

# Estos endpoints son para configurar la BD de producción.

bd_blueprint = Blueprint("bd", __name__, url_prefix="/bd")


@api_blueprint.post("/reset-db")
def reset_db():
    database.reset_db()


@api_blueprint.post("/seeds-db")
def seeds_db():
    seeds.run()
