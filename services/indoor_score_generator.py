from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from models.athlete_comp_data import IndoorScore


def generate_indoor_scores(url, comp_id, comp_year):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        scores = []
        # Find all elements with the target classes
        elements = soup.find_all('tr', class_=["table100-head slim-notresposive top-border", "compressed-group base-background-color bold", "compressed-group alternatingColor bold", "compressed-group base-background-color", "compressed-group alternatingColor"])

        category = ''
        for element in elements:
            th_element = element.find('th')
            if th_element is not None and len(th_element) == 1:
                category = th_element.text.split('[')[0].strip()
            else:
                columns = element.find_all('td')
                indoor_score = IndoorScore(
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
                        nine_score=int(columns[7].text.strip())
                    )
                scores.append(indoor_score)
        return scores
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []     


