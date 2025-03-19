from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class IndoorScore(BaseModel):
    category: str
    comp_id:int
    comp_year:int
    name: str
    position: str
    club_country_code: str
    first_score: int
    second_score: int
    total: int
    ten_score: int
    nine_score: int


class OutdoorScore(BaseModel):
    category: str
    comp_id:int
    comp_year:int
    name: str
    position: str
    club_country_code: str
    first_score: int
    second_score: int
    total: int
    ten_score: int
    x_score: int

class DoubleOutdoorScore(BaseModel):
    category: str
    comp_id:int
    comp_year:int
    name: str
    position: str
    club_country_code: str
    first_score: int
    second_score: int
    third_score: int
    fourth_score: int
    total: int
    ten_score: int
    x_score: int

class AtheleteCompData(BaseModel):
    comp_id:int
    comp_year:int
    comp_type:str
    comp_date:datetime
    category: str
    comp_id:int
    name: str
    position: str
    club_country_code: str
    first_score: int
    second_score: int
    third_score: int
    fourth_score: int
    total: int
    ten_score: int