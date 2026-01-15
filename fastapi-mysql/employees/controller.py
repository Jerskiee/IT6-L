from fastapi import APIRouter, HTTPException
from database import get_db_connection
from . import models, services

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/", response_model=list[models.Employee])
def read_all_employees():
    conn = get_db_connection()
    try:
        return services.get_employees(conn)
    finally:
        conn.close()

@router.get("/{employee_id}", response_model=models.Employee)
def read_one_employee(employee_id: int):
    conn = get_db_connection()
    try:
        payload = models.Employee_ID(id=employee_id)
        employee = services.get_employee_by_id(conn, payload)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    finally:
        conn.close()

@router.post("/")
def create_new_employee(payload: models.Insert_Employee):
    conn = get_db_connection()
    try:
        new_id = services.insert_employee(conn, payload)
        return {"msg": "Employee Registered", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.delete("/{employee_id}")
def remove_employee(employee_id: int):
    conn = get_db_connection()
    try:
        payload = models.Employee_ID(id=employee_id)
        rows = services.delete_employee(conn, payload)
        if rows == 0:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"msg": "Employee Deleted"}
    finally:
        conn.close()