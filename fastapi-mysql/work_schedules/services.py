from . import models

def get_schedules(conn):
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT id, shift_name, 
        CAST(start_time AS CHAR) as start_time, 
        CAST(end_time AS CHAR) as end_time 
        FROM work_schedules
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_schedule_by_id(conn, payload: models.Schedule_ID):
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT id, shift_name, 
        CAST(start_time AS CHAR) as start_time, 
        CAST(end_time AS CHAR) as end_time 
        FROM work_schedules WHERE id = %s
    """
    values = (payload.id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    return result

def insert_schedule(conn, payload: models.Insert_Schedule):
    cursor = conn.cursor()
    query = "INSERT INTO work_schedules (shift_name, start_time, end_time) VALUES (%s, %s, %s)"
    values = (payload.shift_name, payload.start_time, payload.end_time)
    cursor.execute(query, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    return new_id

def delete_schedule(conn, payload: models.Schedule_ID):
    cursor = conn.cursor()
    query = "DELETE FROM work_schedules WHERE id = %s"
    values = (payload.id,)
    cursor.execute(query, values)
    conn.commit()
    rows = cursor.rowcount
    cursor.close()
    return rows