import services.persistance.dbconnect as db_services
from models.competations import CompDetails


db = db_services.get_database()
comp_details = db["comp_details"]



def add_competation(comp: CompDetails):
    generated_comp = {
        "link": comp.link,
        "name": comp.name,
        "location": comp.location,
        "description": comp.description,
        "type": comp.type.value,
        "date": comp.date
    }

    comp_details.insert_one(generated_comp)

def get_competation(comp_id: int):
    return comp_details.find_one({"comp_id": comp_id})
    

def get_competations():
    return comp_details.find()
  