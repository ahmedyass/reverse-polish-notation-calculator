from pydantic import BaseModel
from datetime import datetime

class CalculationCreate(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    id: int
    expression: str
    result: float
    created_at: datetime

    class Config:
        from_attributes = True
