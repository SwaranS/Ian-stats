import requests
from bs4 import BeautifulSoup
import re
from services.indoor_score_generator import generate_indoor_scores
from services.persistance.dbconnect import get_database

url = "https://ianseo.net/TourList.php?Year=2025&countryid=IRL&comptime=&timeType=utc"
#comp_url = "https://ianseo.net/TourInfo.php?TourID="


def process_year_data(comp_country,comp_year):
    comp_list = get_competition_list(year_link_genator(comp_country, comp_year))

    for comp_id in comp_list:
        print(f"Processing Competition ID: {comp_id}")
        print(f"Processing Individual Scores")
        individual_score_link = ind_link_generator(comp_year, comp_id)
        list_of_scores = generate_indoor_scores(individual_score_link,comp_id)
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

