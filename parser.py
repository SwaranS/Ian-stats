import requests
from bs4 import BeautifulSoup
import re

url = "https://ianseo.net/TourList.php?Year=2025&countryid=IRL&comptime=&timeType=utc"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    tr_tags = soup.find_all('tr', class_='cursor-pointer base-background-color')
    details_links = []

    for tr in tr_tags:
        script_tags = tr.find_all('script')
        for script in script_tags:
            if script.string:  # Check if script.string is not None
                matches = re.findall(r"window\.open\('Details\.php\?toId=\d+'\)", script.string)
                for match in matches:
                    details_links.append(match)

    for details_link in details_links:
        print(details_link)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")