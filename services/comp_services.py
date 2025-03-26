import services.persistance.dbconnect as db_services
from models.competations import CompDetailsInput, CompDetails, CompTypes
from models.athlete_comp_data import IndoorScore, OutdoorScore, DoubleOutdoorScore, F1440OutdoorScore, AthleteScores, \
    IndoorScoreOut, OutdoorScoreOut, DoubleOutdoorScoreOut,F1440OutdoorScoreOut
import re
from typing import List
from datetime import datetime
from services.score_services import process_indoor_comp_data, process_outdoor_720_comp_data, process_outdoor_double_720_comp_data,process_outdoor_1440_comp_data

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
    elif comp.type == CompTypes.OUTDOOR_1440:
        process_outdoor_1440_comp_data(comp.year, comp.id)




def get_athlete_data(name: str)-> AthleteScores :

    athlete_scores =  scores.find({"name": name})
    
    indoor_scores : List[IndoorScoreOut] = []
    outdoor_scores : List[OutdoorScoreOut] = []
    double_outdoor_scores : List[DoubleOutdoorScoreOut] = []
    f_1440_scores : List[F1440OutdoorScoreOut] = []

    for s in athlete_scores:
        c_d = get_competition(s["comp_id"], s["comp_year"])
        comp_type_e = CompTypes(c_d["type"]).name
        if comp_type_e == "INDOOR":
            indoor_scores.append(IndoorScoreOut(
                category=s["category"],
                comp_id=s["comp_id"],
                comp_year=s["comp_year"],
                name=s["name"],
                position=s["position"],
                club_country_code=s["club_country_code"],
                first_score=s["first_score"],
                second_score=s["second_score"],
                total=s["total"],
                ten_score=s["ten_score"],
                nine_score=s["nine_score"],
                comp_date=c_d["date"],
                comp_name=c_d["name"]
            ))
        elif comp_type_e == "OUTDOOR_720":
            outdoor_scores.append(OutdoorScoreOut(
                category=s["category"],
                comp_id=s["comp_id"],
                comp_year=s["comp_year"],
                name=s["name"],
                position=s["position"],
                club_country_code=s["club_country_code"],
                first_score=s["first_score"],
                second_score=s["second_score"],
                total=s["total"],
                ten_score=s["ten_score"],
                x_score=s["x_score"],
                comp_date=c_d["date"],
                comp_name=c_d["name"]
            ))
        elif comp_type_e == "OUTDOOR_Double_720":
            double_outdoor_scores.append(DoubleOutdoorScoreOut(
                category=s["category"],
                comp_id=s["comp_id"],
                comp_year=s["comp_year"],
                name=s["name"],
                position=s["position"],
                club_country_code=s["club_country_code"],
                first_score=s["first_score"],
                second_score=s["second_score"],
                third_score=s["third_score"],
                fourth_score=s["fourth_score"],
                total=s["total"],
                ten_score=s["ten_score"],
                x_score=s["x_score"],
                comp_date=c_d["date"],
                comp_name=c_d["name"]
            ))
        elif comp_type_e == "OUTDOOR_1440":
            f_1440_scores.append(F1440OutdoorScoreOut(
                category=s["category"],
                comp_id=s["comp_id"],
                comp_year=s["comp_year"],
                name=s["name"],
                position=s["position"],
                club_country_code=s["club_country_code"],
                first_score=s["first_score"],
                second_score=s["second_score"],
                third_score=s["third_score"],
                fourth_score=s["fourth_score"],
                total=s["total"],
                ten_score=s["ten_score"],
                x_score=s["x_score"],
                comp_date=c_d["date"],
                comp_name=c_d["name"]
            ))
    return AthleteScores(
        indoor_scores=indoor_scores,
        outdoor_scores=outdoor_scores,
        double_outdoor_scores=double_outdoor_scores,
        f_1440_scores=f_1440_scores
    )

    
    

def get_competition(id: int, year: int):
    return comp_details.find_one({"comp_id": id, "year": year})

from typing import List

def get_competitions():
    return comp_details.find({"id": int})


def get_available_athletes() -> List[str]:
    athletes = scores.distinct("name")
    return athletes