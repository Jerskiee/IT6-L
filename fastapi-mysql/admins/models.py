from pydantic import BaseModel

class Insert_Admin(BaseModel):
    email: str
    password: str

class Admin_ID(BaseModel):
    id: int

class Admin(BaseModel):
    id: int
    email: str
    password: str