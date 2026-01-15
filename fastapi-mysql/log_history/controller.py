from fastapi import APIRouter, HTTPException
from database import get_db_connection
from . import models, services

router = APIRouter(prefix="/logs", tags=["Log History"])

@router.get("/", response_model=list[models.Log])
def read_all_logs():
    conn = get_db_connection()
    try:
        return services.get_logs(conn)
    finally:
        conn.close()

@router.get("/{log_id}", response_model=models.Log)
def read_one_log(log_id: int):
    conn = get_db_connection()
    try:
        payload = models.Log_ID(id=log_id)
        log = services.get_log_by_id(conn, payload)
        if not log:
            raise HTTPException(status_code=404, detail="Log not found")
        return log
    finally:
        conn.close()

@router.post("/")
def create_log(payload: models.Insert_Log):
    conn = get_db_connection()
    try:
        
        
        new_id = services.insert_log(conn, payload)
        return {"msg": "Log Created", "id": new_id}
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.delete("/{log_id}")
def remove_log(log_id: int):
    conn = get_db_connection()
    try:
        payload = models.Log_ID(id=log_id)
        rows = services.delete_log(conn, payload)
        if rows == 0:
            raise HTTPException(status_code=404, detail="Log not found")
        return {"msg": "Log Deleted"}
    finally:
        conn.close()