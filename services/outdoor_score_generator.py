from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import re
from models.athlete_comp_data import OutdoorScore, DoubleOutdoorScore, F1440OutdoorScore


def generate_outdoor_scores(url, comp_year,comp_id):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        scores = []
        
        elements = soup.find_all('tr', class_=["table100-head slim-notresposive top-border", "compressed-group base-background-color bold", "compressed-group alternatingColor bold", "compressed-group base-background-color", 
                                               "compressed-group alternatingColor","slim-subheaders text-right mobile-noshow"])
        category = ''
        for element in elements:
            th_element = element.find('th')
            if th_element is not None and len(th_element) == 1:
                category = th_element.text.split('[')[0].strip()
            else:
                columns = element.find_all('td')
                if len(columns) >= 8:  # Ensure there are enough columns
                    outdoor_score = OutdoorScore(
                        category=category,
                        comp_id=comp_id,
                        comp_year=comp_year,
                        position=str(columns[0].text.strip()),
                        name=columns[1].text.strip(),
                        club_country_code=columns[2].text.strip(),
                        first_score=int(columns[3].text.strip().split('/')[0]),
                        second_score=int(columns[4].text.strip().split('/')[0]),
                        total=int(columns[5].text.strip()),
                        ten_score=int(columns[6].text.strip()),
                        x_score=int(columns[7].text.strip())
                    )
                    scores.append(outdoor_score)
        return scores
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

def generate_double_720_scores(url, comp_year,comp_id):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        scores = []
        
        elements = soup.find_all('tr', class_=["table100-head slim-notresposive top-border", "compressed-group base-background-color bold", "compressed-group alternatingColor bold", "compressed-group base-background-color", 
                                               "compressed-group alternatingColor","slim-subheaders text-right mobile-noshow"])
        category = ''
        for element in elements:
            th_element = element.find('th')
            if th_element is not None and len(th_element) == 1:
                category = th_element.text.split('[')[0].strip()
            else:
                columns = element.find_all('td')
                if len(columns) >= 8:  # Ensure there are enough columns
                    outdoor_score = DoubleOutdoorScore(
                        category=category,
                        comp_id=comp_id,
                        comp_year = comp_year,
                        position=str(columns[0].text.strip()),
                        name=columns[1].text.strip(),
                        club_country_code=columns[2].text.strip(),
                        first_score=int(columns[3].text.strip().split('/')[0]),
                        second_score=int(columns[4].text.strip().split('/')[0]),
                        third_score=int(columns[5].text.strip().split('/')[0]),
                        fourth_score=int(columns[6].text.strip().split('/')[0]),
                        total=int(columns[7].text.strip()),
                        ten_score=int(columns[8].text.strip()),
                        x_score=int(columns[9].text.strip())
                    )
                    scores.append(outdoor_score)
        return scores
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []
    
def generate_1440_scores(url, comp_year,comp_id):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        scores = []
        
        elements = soup.find_all('tr', class_=["table100-head slim-notresposive top-border", "compressed-group base-background-color bold", "compressed-group alternatingColor bold", "compressed-group base-background-color", 
                                               "compressed-group alternatingColor","slim-subheaders text-right mobile-noshow"])
        category = ''
        for element in elements:
            th_element = element.find('th')
            if th_element is not None and len(th_element) == 1:
                category = th_element.text.split('[')[0].strip()
            else:
                columns = element.find_all('td')
                if len(columns) >= 8:  # Ensure there are enough columns
                    outdoor_score = F1440OutdoorScore(
                        category=category,
                        comp_id=comp_id,
                        comp_year = comp_year,
                        position=str(columns[0].text.strip()),
                        name=columns[1].text.strip(),
                        club_country_code=columns[2].text.strip(),
                        first_score=int(columns[3].text.strip().split('/')[0]),
                        second_score=int(columns[4].text.strip().split('/')[0]),
                        third_score=int(columns[5].text.strip().split('/')[0]),
                        fourth_score=int(columns[6].text.strip().split('/')[0]),
                        total=int(columns[7].text.strip()),
                        ten_score=int(columns[8].text.strip()),
                        x_score=int(columns[9].text.strip())
                    )
                    scores.append(outdoor_score)
        return scores
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []