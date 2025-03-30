from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CalculationCreate(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    id: int
    expression: str
    result: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
