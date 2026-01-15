import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="attendance_system",
        port=3306,
        use_pure=True,          # <--- THIS IS THE MAGIC FIX
        connection_timeout=5    
    )