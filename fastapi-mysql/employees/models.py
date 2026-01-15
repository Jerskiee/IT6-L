from pydantic import BaseModel

class Insert_Employee(BaseModel):
    name: str
    email: str
    password: str
    work_hours_id: int
    admin_id: int

class Employee_ID(BaseModel):
    id: int

class Employee(BaseModel):
    id: int
    name: str
    email: str
    password: str
    work_hours_id: int
    admin_id: int