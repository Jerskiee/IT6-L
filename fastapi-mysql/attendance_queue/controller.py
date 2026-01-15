import venv
from fastapi import APIRouter, HTTPException
from database import get_db_connection
from . import models, services

router = APIRouter(prefix="/attendance", tags=["Attendance Queue"])

@router.get("/", response_model=list[models.Queue])
def read_all_attendance():
    conn = get_db_connection()
    try:
        return services.get_queue(conn)
    finally:
        conn.close()

@router.get("/{queue_id}", response_model=models.Queue)
def read_one_attendance(queue_id: int):
    conn = get_db_connection()
    try:
        payload = models.Queue_ID(id=queue_id)venv\Scripts\activate
        queue = services.get_queue_by_id(conn, payload)
        if not queue:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        return queue
    finally:
        conn.close()

@router.post("/")
def create_attendance(payload: models.Insert_Queue):
    conn = get_db_connection()
    try:
        new_id = services.insert_queue(conn, payload)
        return {"msg": "Attendance Logged", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.delete("/{queue_id}")
def remove_attendance(queue_id: int):
    conn = get_db_connection()
    try:
        payload = models.Queue_ID(id=queue_id)
        rows = services.delete_queue(conn, payload)
        if rows == 0:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        return {"msg": "Attendance Deleted"}
    finally:
        conn.close()