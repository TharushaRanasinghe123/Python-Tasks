from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    name: str
    email: str
    age: int
    position: str
    department: str
    salary: float
    join_date: Optional[str] = None