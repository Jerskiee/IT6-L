from pydantic import BaseModel

class Insert_Schedule(BaseModel):
    shift_name: str
    start_time: str  
    end_time: str    

class Schedule_ID(BaseModel):
    id: int

class Schedule(BaseModel):
    id: int
    shift_name: str
    start_time: str
    end_time: str