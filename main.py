from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services import comp_services
from models.competations import CompDetailsInput
from typing import List
from services.score_services import process_indoor_comp_data, process_outdoor_720_comp_data
from services.comp_services import get_athlete_data


app = FastAPI()

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="static")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/add_scores/{comp_id}/{comp_year}")
async def add_scores(comp_id: int, comp_year: int):
    list_of_scores = process_indoor_comp_data(comp_year, comp_id)
    return {"scores":list_of_scores}

@app.get("/add_outdoor_scores/{comp_id}/{comp_year}")
async def add_outdoor_scores(comp_id: int, comp_year: int):
    list_of_scores = process_outdoor_720_comp_data(comp_year, comp_id)
    return {"scores":list_of_scores}

@app.get("/get_ath_date/{name}")
async def add_outdoor_scores(name: str):
    list_of_scores = get_athlete_data(name)
    return {"scores":list_of_scores}

@app.get("/add_comp", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("add_comp.html", {"request": request})

@app.post("/add_competation_data")
async def add_competation_data(comp_details: List[CompDetailsInput]):
    for comp in comp_details:
        comp_services.add_competition(comp)
    
    return {"message":"Added Competation Data"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

