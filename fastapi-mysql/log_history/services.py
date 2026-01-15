from . import models

def get_logs(conn):
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT id, employee_id, action_type, description, 
        CAST(created_at AS CHAR) as created_at 
        FROM log_history
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_log_by_id(conn, payload: models.Log_ID):
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT id, employee_id, action_type, description, 
        CAST(created_at AS CHAR) as created_at 
        FROM log_history WHERE id = %s
    """
    values = (payload.id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    return result

def insert_log(conn, payload: models.Insert_Log):
    cursor = conn.cursor()
    
    query = "INSERT INTO log_history (employee_id, action_type, description) VALUES (%s, %s, %s)"
    values = (payload.employee_id, payload.action_type, payload.description)
    cursor.execute(query, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def delete_log(conn, payload: models.Log_ID):
    cursor = conn.cursor()
    query = "DELETE FROM log_history WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    conn.commit()
    rows = cursor.rowcount
    cursor.close()
    return rows