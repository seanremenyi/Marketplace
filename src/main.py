from flask import Flask, request, jsonify, abort
app = Flask(__name__)
import psycopg2

connection = psycopg2.connect(
    database="marketplace",
    user="postgres",
    password="bW3JmgqX5ZDtWpPJ",
    host="3.26.33.173",
    port=5432
    )

cursor = connection.cursor()
cursor.execute("create table if not exists books (id serial Primary KEY, name varchar);")

@app.route("/items", methods=["GET"])
def item_index():
    sql = "SELECT * FROM items;"
    cursor.execute(sql)
    items=cursor.fetchall()
    return jsonify(items)

@app.route("/items", methods=["POST"])
def item_create():
    sql = "INSERT INTO items (name) VALUES (%s);"
    cursor.execute(sql, (request.json["name"],))
    connection.commit()
    
    sql = "SELECT * FROM items ORDER BY ID DESC LIMIT 1;"
    cursor.execute(sql)
    item = cursor.fetchone()
    return jsonify(item)



@app.route("/items/<int:id>", methods=["GET"])
def item_show(id):
    sql = f"SELECT * FROM items WHERE id = %s;"
    cursor.execute(sql, (id,))
    item = cursor.fetchone()
    return jsonify(item)



@app.route("/items/<int:id>", methods=["PUT", "PATCH"])
def item_update(id):
    sql= "UPDATE items SET name = %s where id = %s;"
    cursor.execute(sql, (request.json["name"], id))
    connection.commit()
    
    sql = "SELECT * FROM items where id = %s;"
    cursor.execute(sql, (id,))
    items = cursor.fetchone()
    return jsonify(items)
    

@app.route("/items/<int:id>", methods=["DELETE"])
def item_delete(id):
    sql = "DELETE FROM ITEMS where id = %s;"
    cursor.execute(sql, (id,))
    item = cursor.fetchone()
    
    if item:
        sql = "DELETE FROM items where id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()
        
    return jsonify(item)



# def add(a,b):
#     return (a+b)
    

