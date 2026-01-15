from . import models

def get_admins(conn):
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM admins"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_admin_by_id(conn, payload: models.Admin_ID):
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM admins WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    return result

def insert_admin(conn, payload: models.Insert_Admin):
    cursor = conn.cursor()
    query = "INSERT INTO admins (email, password) VALUES (%s, %s)"
    values = (payload.email, payload.password)
    cursor.execute(query, values)
    conn.commit()  
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def delete_admin(conn, payload: models.Admin_ID):
    cursor = conn.cursor()
    query = "DELETE FROM admins WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    conn.commit()  
    rows = cursor.rowcount
    cursor.close()
    return rows