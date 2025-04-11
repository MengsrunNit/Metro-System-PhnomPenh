from pydantic import BaseModel

class StationCreate(BaseModel): 
    name: str
    line: str
    long: float 
    lat: float
    

class StationOut(StationCreate): 
    id: int