from pydantic import BaseModel
from typing import Optional

class StationCreate(BaseModel): 
    name: str
    line_id: Optional[int]  #Referential to Line
    lon: float  
    lat: float

class StationOut(StationCreate): 
    id: int

    class Config:
        orm_mode = True
