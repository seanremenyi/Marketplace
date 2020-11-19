from main import ma
from models.Items import Item

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)