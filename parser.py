import requests
from bs4 import BeautifulSoup
import re

url = "https://ianseo.net/TourList.php?Year=2025&countryid=IRL&comptime=&timeType=utc"
comp_url = "https://ianseo.net/TourInfo.php?TourID="

response = requests.get(url)

def get_competation_list():
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

def ind_link_genator(comp_year,comp_id):
    return f"https://ianseo.net/TourData/{comp_year}/{comp_id}/IC.php"

def team_link_genator(comp_year,comp_id):
    return f"https://ianseo.net/TourData/{comp_year}/{comp_id}/IC.php"

print(ind_link_genator(2025,21763))