# Create model for route
from pydantic import BaseModel

class RouteCreate(BaseModel):
    start_station_id: int
    end_station_id: int
    line_id: int
    distance_km: float

class RouteOut(RouteCreate):
    id: int

    class Config:
        orm_mode = True  # Allows model to read data from ORM objects
