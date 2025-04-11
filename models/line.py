# Create model for Line

from pydantic import BaseModel

class LineCreate(BaseModel):
    name: str
    color: str
    type: str = "linear"

class LineOut(LineCreate):
    id: int

    # Allows model to read data from ORM objects (e.g., SQLAlchemy)
    class Config:
        orm_mode = True
