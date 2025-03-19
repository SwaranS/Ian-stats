import services.persistance.dbconnect as db_services
from models.competations import CompDetailsInput, CompDetails, CompTypes
from models.athlete_comp_data import AtheleteCompData
import re
from typing import List
from datetime import datetime
from services.score_services import process_indoor_comp_data, process_outdoor_720_comp_data, process_outdoor_double_720_comp_data

db = db_services.get_database()
comp_details = db["comp_details"]
scores = db["scores"]

def extract_comp_id(url: str) -> int:
    match = re.search(r'toId=(\d+)', url)
    if match:
        return int(match.group(1))
    return 0

def add_competition(comp: CompDetailsInput):
    id = extract_comp_id(comp.link)
    generated_comp = CompDetails(
        id=id,
        name=comp.name,
        location=comp.location,
        description=comp.description,
        type=comp.type.value,
        date=comp.date,
        year=comp.date.year
    )
    insert_comp_data(generated_comp)
    comp_details.update_one(
        {"comp_id": id, "year": comp.date.year},
        {"$set": {
            "name": comp.name,
            "location": comp.location,
            "description": comp.description,
            "type": comp.type.value,
            "date": comp.date,
            "year": comp.date.year
        }},
        upsert=True
    )

def insert_comp_data(comp: CompDetails):
    if comp.type == CompTypes.INDOOR:
        process_indoor_comp_data(comp.year, comp.id)
    elif comp.type == CompTypes.OUTDOOR_720:
        process_outdoor_720_comp_data(comp.year, comp.id)
    elif comp.type == CompTypes.OUTDOOR_Double_720:
        process_outdoor_double_720_comp_data(comp.year, comp.id)



def get_athlete_data(name: str)-> List[AtheleteCompData] :
    athlete_scores =  scores.find({"name": name})
    athlete_data_list = []
    for s in athlete_scores:
        comp_details = get_competition(s["comp_id"], s["comp_year"])
        comp_type_e = CompTypes(comp_details["type"]).name

        athlete_data = AtheleteCompData(
            name=s["name"],
            comp_id=s["comp_id"],
            comp_year=s["comp_year"],
            comp_type=comp_type_e,
            comp_date=comp_details["date"],
            category=s["category"],
            position=s.get("position", 0),
            club_country_code=s["club_country_code"],
            first_score=s.get("first_score", 0),
            second_score=s.get("second_score", 0),
            third_score=s.get("third_score", 0),
            fourth_score=s.get("fourth_score", 0),
            total=s.get("total", 0),
            ten_score=s.get("ten_score", 0)
        )
        athlete_data_list.append(athlete_data)
    return athlete_data_list
    
    

def get_competition(id: int, year: int):
    return comp_details.find_one({"comp_id": id, "year": year})

from typing import List

def get_competitions():
    return comp_details.find({"id": int})