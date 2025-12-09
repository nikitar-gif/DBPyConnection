from db import create_connection

def insert_user(name, email):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO dummy_table (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print("Record inserted successfully.")

def get_users():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dummy_table")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows


