from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class CompTypes(Enum):
    INDOOR = 1
    OUTDOOR_720 = 2
    OUTDOOR_720_2 = 3


class CompDetails(BaseModel):
    link:str
    name: str
    location: str
    description:str
    type: CompTypes
    date: datetime