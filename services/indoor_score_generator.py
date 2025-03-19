from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from models.athlete_comp_data import IndoorScore


def generate_indoor_scores(url,comp_id):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        scores = []
        # Find all elements with the target class
        #elements = soup.find_all(class_="compressed-group base-background-color bold")
        elements = soup.find_all('tr', class_=["compressed-group base-background-color bold", "compressed-group alternatingColor bold","compressed-group base-background-color", "compressed-group alternatingColor"])


        for element in elements:
            columns = element.find_all('td')

            indoor_score = IndoorScore(
                comp_id=comp_id,
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


