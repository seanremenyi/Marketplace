# import psycopg2

# connection = psycopg2.connect(
#     database="marketplace",
#     user="postgres",
#     password="bW3JmgqX5ZDtWpPJ",
#     host="3.26.33.173",
#     port=5432
#     )

# cursor = connection.cursor()
# cursor.execute("create table if not exists books (id serial Primary KEY, name varchar);")

from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:bW3JmgqX5ZDtWpPJ@3.26.33.173:5432/marketplace"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db