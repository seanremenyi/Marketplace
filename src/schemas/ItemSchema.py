from main import ma
from models.Items import Item
from marshmallow.validate import Length

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        
    title = ma.String(required=True, validate=Length(min=1))
    cost = ma.Integer(required=True)
        
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)