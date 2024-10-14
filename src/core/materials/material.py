from datetime import datetime
from src.core.database import db


"""
mi modelo de datos que se va a corrresponder 1 a 1 con la bd
"""

class Material(db.Model):
    """
    modelo de material
    cada material tendrá un id y un nombre, el nombre se utilizará para las consultas y el id para las reservas
    """
    __tablename__ = "materials"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(255))
    
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)