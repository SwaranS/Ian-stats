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

class IndoorScoreOut(IndoorScore):  
    comp_date: datetime
    comp_name: str    


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

class OutdoorScoreOut(OutdoorScore):  
    comp_date: datetime
    comp_name: str 

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


class DoubleOutdoorScoreOut(DoubleOutdoorScore):
    comp_date: datetime
    comp_name: str

class F1440OutdoorScore(BaseModel):
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

class F1440OutdoorScoreOut(F1440OutdoorScore):
   comp_date: datetime
   comp_name: str   



class AthleteScores(BaseModel):
    indoor_scores: list[IndoorScoreOut]
    outdoor_scores: list[OutdoorScoreOut]
    double_outdoor_scores: list[DoubleOutdoorScoreOut]
    f_1440_scores: list[F1440OutdoorScoreOut]
