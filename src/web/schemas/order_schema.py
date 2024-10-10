from marshmallow import Schema
from marshmallow import fields


class OrderSchema(Schema):
    # id=fields.Int()
    material = fields.Str()
    cantidad = fields.Float()


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
