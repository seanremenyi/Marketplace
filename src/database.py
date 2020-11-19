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