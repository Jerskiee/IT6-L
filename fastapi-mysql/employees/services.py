from . import models

def get_employees(conn):
    
    cursor = conn.cursor(dictionary=True) 
    query = "SELECT * FROM employees"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_employee_by_id(conn, payload: models.Employee_ID):
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM employees WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    return result

def insert_employee(conn, payload: models.Insert_Employee):
    cursor = conn.cursor()
    query = "INSERT INTO employees (name, email, password, work_hours_id, admin_id) VALUES (%s, %s, %s, %s, %s)"
    values = (payload.name, payload.email, payload.password, payload.work_hours_id, payload.admin_id)
    cursor.execute(query, values)
    conn.commit()  
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def delete_employee(conn, payload: models.Employee_ID):
    cursor = conn.cursor()
    query = "DELETE FROM employees WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    conn.commit()  
    rows = cursor.rowcount
    cursor.close()
    return rows