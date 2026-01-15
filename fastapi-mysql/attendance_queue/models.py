from pydantic import BaseModel
from typing import Optional

class Insert_Queue(BaseModel):
    employee_id: int
    work_hours_id: int
    date: str           
    time: str           
    status: str         
    reason_for_late: Optional[str] = None

class Queue_ID(BaseModel):
    id: int

class Queue(BaseModel):
    id: int
    employee_id: int
    work_hours_id: int
    date: str
    time: str
    status: str
    reason_for_late: Optional[str] = None