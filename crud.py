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

# def update_user(user_id, name, email):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         query = "UPDATE dummy_table SET name=%s, email=%s WHERE id=%s"
#         values = (name, email, user_id)
#         cursor.execute(query, values)
#         connection.commit()
#         cursor.close()
#         connection.close()
#         print("Record updated successfully.")

# def delete_user(user_id):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         query = "DELETE FROM dummy_table WHERE id=%s"
#         cursor.execute(query, (user_id,))
#         connection.commit()
#         cursor.close()
#         connection.close()
#         print("Record deleted successfully.")
