from models.Items import Item
from main import db
from schemas.ItemSchema import item_schema, items_schema
from flask import Blueprint, request, jsonify
items = Blueprint('items', __name__, url_prefix="/items")

@items.route("/", methods=["GET"])
def item_index():
    items= Item.query.all()
    return jsonify(items_schema.dump(items))


@items.route("/", methods=["POST"])
def item_create():
    item_fields = item_schema.load(request.json)
    
    new_item = Item()
    new_item.name = item_fields["name"]
    
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify(item_schema.dump(new_item))



@items.route("/<int:id>", methods=["GET"])
def item_show(id):
    item = Item.query.get(id)
    return jsonify(item_schema.dump(item))


@items.route("/<int:id>", methods=["PUT", "PATCH"])
def item_update(id):
    items = Item.query.filter_by(id=id)
    item_fields = item_schema.load(request.json)
    items.update(item_fields)
    db.session.commit()
    
    return jsonify(item_schema.dump(items[0]))
    

@items.route("/<int:id>", methods=["DELETE"])
def item_delete(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    
    return jsonify(item_schema.dump(item))