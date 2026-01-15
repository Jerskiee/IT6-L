from fastapi import APIRouter, HTTPException
from database import get_db_connection
from . import models, services

router = APIRouter(prefix="/work_schedules", tags=["Work Schedules"])

@router.get("/", response_model=list[models.Schedule])
def read_all_schedules():
    conn = get_db_connection()
    try:
        return services.get_schedules(conn)
    finally:
        conn.close()

@router.get("/{schedule_id}", response_model=models.Schedule)
def read_one_schedule(schedule_id: int):
    conn = get_db_connection()
    try:
        payload = models.Schedule_ID(id=schedule_id)
        schedule = services.get_schedule_by_id(conn, payload)
        if not schedule:
            raise HTTPException(status_code=404, detail="Schedule not found")
        return schedule
    finally:
        conn.close()

@router.post("/")
def create_schedule(payload: models.Insert_Schedule):
    conn = get_db_connection()
    try:
        new_id = services.insert_schedule(conn, payload)
        return {"msg": "Schedule Created", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.delete("/{schedule_id}")
def remove_schedule(schedule_id: int):
    conn = get_db_connection()
    try:
        payload = models.Schedule_ID(id=schedule_id)
        rows = services.delete_schedule(conn, payload)
        if rows == 0:
            raise HTTPException(status_code=404, detail="Schedule not found")
        return {"msg": "Schedule Deleted"}
    finally:
        conn.close()