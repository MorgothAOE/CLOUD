from datetime import datetime
from src.core.database import db


"""
mi modelo de datos que se va a corrresponder 1 a 1 con la bd
"""

class Order(db.Model):
    """
    modelo de orden/pedido
    contempla que se va hacer un pedido por material ya que los distintos depositos podrian no manejar todos los materiales
    """
    __tablename__ = "orders"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    cantidad = db.Column(db.Float)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), default=0)
    entregado = db.Column(db.Boolean, default=False)
    material = db.relationship("Material", backref="orders")
    provider = db.relationship("Provider", backref="providers")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
