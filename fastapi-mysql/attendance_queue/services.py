from . import models

def get_queue(conn):
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT id, employee_id, work_hours_id, status, reason_for_late,
        CAST(date AS CHAR) as date, 
        CAST(time AS CHAR) as time 
        FROM attendance_queue
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_queue_by_id(conn, payload: models.Queue_ID):
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT id, employee_id, work_hours_id, status, reason_for_late,
        CAST(date AS CHAR) as date, 
        CAST(time AS CHAR) as time 
        FROM attendance_queue WHERE id = %s
    """
    values = (payload.id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    return result

def insert_queue(conn, payload: models.Insert_Queue):
    cursor = conn.cursor()
    query = """
        INSERT INTO attendance_queue 
        (employee_id, work_hours_id, date, time, status, reason_for_late) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        payload.employee_id, 
        payload.work_hours_id, 
        payload.date, 
        payload.time, 
        payload.status, 
        payload.reason_for_late
    )
    cursor.execute(query, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def delete_queue(conn, payload: models.Queue_ID):
    cursor = conn.cursor()
    query = "DELETE FROM attendance_queue WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    conn.commit()
    rows = cursor.rowcount
    cursor.close()
    return rows