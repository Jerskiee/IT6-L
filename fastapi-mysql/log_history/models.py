from pydantic import BaseModel


class Insert_Log(BaseModel):
    employee_id: int
    action_type: str
    description: str

class Log_ID(BaseModel):
    id: int

class Log(BaseModel):
    id: int
    employee_id: int
    action_type: str
    description: str
    created_at: str  