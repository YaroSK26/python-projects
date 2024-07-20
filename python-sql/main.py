from psycopg2 import pool

db_pool = pool.SimpleConnectionPool(1,10, dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432")

def create_table():
    with db_pool.getconn() as connection:
        with connection.cursor() as cur:
            cur.execute('''CREATE TABLE teacher(
                ID SERIAL,
                NAME TEXT NOT NULL,
                AGE INT NOT NULL,
                ADDRESS TEXT
    )''')
            connection.commit()
            db_pool.putconn(connection)

def insert():
     with db_pool.getconn() as connection:
        with connection.cursor() as cur:
            name = input("meno:")
            age = input("rok:")
            address = input("addresa:")

            query =  "INSERT INTO teacher (name, age, address) VALUES (%s, %s, %s)"
            cur.execute(query, (name, age, address))
            connection.commit()
            db_pool.putconn(connection)
            print("Insert successfully.")
insert()