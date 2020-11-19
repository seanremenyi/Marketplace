from database import cursor, connection
from flask import Blueprint, request, jsonify
items = Blueprint('items', __name__, url_prefix="/items")

@items.route("/", methods=["GET"])
def item_index():
    sql = "SELECT * FROM items;"
    cursor.execute(sql)
    items=cursor.fetchall()
    return jsonify(items)

@items.route("/", methods=["POST"])
def item_create():
    sql = "INSERT INTO items (name) VALUES (%s);"
    cursor.execute(sql, (request.json["name"],))
    connection.commit()
    
    sql = "SELECT * FROM items ORDER BY ID DESC LIMIT 1;"
    cursor.execute(sql)
    item = cursor.fetchone()
    return jsonify(item)



@items.route("/<int:id>", methods=["GET"])
def item_show(id):
    sql = f"SELECT * FROM items WHERE id = %s;"
    cursor.execute(sql, (id,))
    item = cursor.fetchone()
    return jsonify(item)



@items.route("/<int:id>", methods=["PUT", "PATCH"])
def item_update(id):
    sql= "UPDATE items SET name = %s where id = %s;"
    cursor.execute(sql, (request.json["name"], id))
    connection.commit()
    
    sql = "SELECT * FROM items where id = %s;"
    cursor.execute(sql, (id,))
    items = cursor.fetchone()
    return jsonify(items)
    

@items.route("/<int:id>", methods=["DELETE"])
def item_delete(id):
    sql = "DELETE FROM ITEMS where id = %s;"
    cursor.execute(sql, (id,))
    item = cursor.fetchone()
    
    if item:
        sql = "DELETE FROM items where id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()
        
    return jsonify(item)