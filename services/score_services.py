import requests
from bs4 import BeautifulSoup
import re
from services.indoor_score_generator import generate_indoor_scores
from services.outdoor_score_generator import generate_outdoor_scores, generate_double_720_scores, generate_1440_scores
import services.persistance.dbconnect as db_services

db = db_services.get_database()
scores = db["scores"]


url = "https://ianseo.net/TourList.php?Year=2025&countryid=IRL&comptime=&timeType=utc"
#comp_url = "https://ianseo.net/TourInfo.php?TourID="


def process_indoor_comp_data(comp_year, comp_id):
    individual_score_link = ind_link_generator(comp_year, comp_id)
    list_of_scores = generate_indoor_scores(individual_score_link,comp_year,comp_id)
    for score in list_of_scores:    
        scores.insert_one(score.dict())
        

def process_outdoor_720_comp_data(comp_year, comp_id):
    individual_score_link = ind_link_generator(comp_year, comp_id)
    list_of_scores = generate_outdoor_scores(individual_score_link,comp_year,comp_id)
    for score in list_of_scores:    
        scores.insert_one(score.dict())
        

def process_outdoor_double_720_comp_data(comp_year, comp_id):
    individual_score_link = ind_link_generator(comp_year, comp_id)
    list_of_scores = generate_double_720_scores(individual_score_link,comp_year,comp_id)
    for score in list_of_scores:    
        scores.insert_one(score.dict())

def process_outdoor_1440_comp_data(comp_year, comp_id):
    individual_score_link = ind_link_generator(comp_year, comp_id)
    list_of_scores = generate_1440_scores(individual_score_link,comp_year,comp_id)
    scores.delete_many({"comp_id":comp_id,"comp_year": comp_year})
    for score in list_of_scores:    
        scores.insert_one(score.dict())


def process_year_data(comp_country,comp_year,comp_date):
    comp_list = get_competition_list(year_link_genator(comp_country, comp_year))

    for comp_id in comp_list:
        print(f"Processing Competition ID: {comp_id}")
        print(f"Processing Individual Scores")
        individual_score_link = ind_link_generator(comp_year, comp_id)
        list_of_scores = generate_indoor_scores(individual_score_link,comp_id,comp_year,comp_date)
        for score in list_of_scores:    
            print(score)


def get_competition_list(comp_url):
    response = requests.get(comp_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tr_tags = soup.find_all('tr', class_='cursor-pointer base-background-color')
        details_links = []

        for tr in tr_tags:
            onclick_attr = tr.get('onclick')
            if onclick_attr:
                match = re.search(r'toId=(\d+)', onclick_attr)
                match = match.group(1) if match else None
                if match:   
                    details_links.append(match)
        return details_links

def ind_link_generator(comp_year, comp_id):
    return f"https://ianseo.net/TourData/{comp_year}/{comp_id}/IC.php"

def team_link_generator(comp_year, comp_id):
    return f"https://ianseo.net/TourData/{comp_year}/{comp_id}/IC.php"

#Example Output: https://ianseo.net/TourList.php?Year=2025&countryid=IRL&comptime=&timeType=utc
def year_link_genator(comp_country,comp_year):
    return f"https://ianseo.net/TourList.php?Year={comp_year}&countryid={comp_country}&comptime=&timeType=utc"

