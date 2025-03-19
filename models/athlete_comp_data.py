from pydantic import BaseModel

class IndoorScore(BaseModel):
    comp_id:int
    name: str
    position: str
    club_country_code: str
    first_score: int
    second_score: int
    total: int
    ten_score: int
    nine_score: int