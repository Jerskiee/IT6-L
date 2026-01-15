from fastapi import APIRouter, HTTPException
from database import get_db_connection
from . import models, services

router = APIRouter(prefix="/admins", tags=["Admins"])

@router.get("/", response_model=list[models.Admin])
def read_all_admins():
    conn = get_db_connection()
    try:
        return services.get_admins(conn)
    finally:
        conn.close()

@router.get("/{admin_id}", response_model=models.Admin)
def read_one_admin(admin_id: int):
    conn = get_db_connection()
    try:
        payload = models.Admin_ID(id=admin_id)
        admin = services.get_admin_by_id(conn, payload)
        if not admin:
            raise HTTPException(status_code=404, detail="Admin not found")
        return admin
    finally:
        conn.close()

@router.post("/")
def create_admin(payload: models.Insert_Admin):
    conn = get_db_connection()
    try:
        new_id = services.insert_admin(conn, payload)
        return {"msg": "Admin Registered", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.delete("/{admin_id}")
def remove_admin(admin_id: int):
    conn = get_db_connection()
    try:
        payload = models.Admin_ID(id=admin_id)
        rows = services.delete_admin(conn, payload)
        if rows == 0:
            raise HTTPException(status_code=404, detail="Admin not found")
        return {"msg": "Admin Deleted"}
    finally:
        conn.close()