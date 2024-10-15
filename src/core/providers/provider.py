from datetime import datetime
from src.core.database import db
from src.core.materials.material import Material


"""
mi modelo de datos que se va a corrresponder 1 a 1 con la bd
"""

class Provider(db.Model):
    """
    modelo de proveedor; para registrar los proveedores de cada material
    """
    __tablename__ = "providers"
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255))
    nombre_deposito = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)



class MaterialProvider(db.Model):
    """
    modelo para consultar los proveedores de cada material
    """
    __tablename__="material_providers"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'), default=0)
    material = db.relationship("Material", backref="orders")
    provider = db.relationship("Provider", backref="providers")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)