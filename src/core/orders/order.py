from datetime import datetime
from src.core.database import db
from src.core.materials.material import Material
from src.core.providers.provider import Provider


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
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'), nullable=False)
    cantidad = db.Column(db.Float)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'), default=-1)
    entregado = db.Column(db.Boolean, default=False)
    #material = db.relationship("Material", backref="orders")
    #provider = db.relationship("Provider", backref="providers")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    
    def to_dict(self):
        return {
            'id': self.id,
            'material_id': self.material_id,
            'cantidad': self.cantidad,
            'provider_id': self.provider_id,
            'entregado': self.entregado,
            'updated_at': self.updated_at,
            'inserted_at': self.inserted_at
        }

