from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class CompTypes(Enum):
    INDOOR = 1
    OUTDOOR_720 = 2
    OUTDOOR_Double_720 = 3


class CompDetailsInput(BaseModel):
    link:str
    name: str
    location: str
    description:str
    type: CompTypes
    date: datetime

class CompDetails(BaseModel):
    id:int
    name: str
    location: str
    description:str
    type: CompTypes
    date: datetime
    year: int    