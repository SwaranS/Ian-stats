import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = 'https://www.ianseo.net/TourData/2024/18288/IC.php'

# Send a GET request to fetch the webpage content
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status codes

# Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing 'Recurve - Men'
recurve_men_section = soup.find('h2', string='Recurve - Men')

# Initialize a list to store the athlete names
athlete_names = []

# If the section is found, proceed to extract names
if recurve_men_section:
    # The table containing the data is typically right after the heading
    table = recurve_men_section.find_next('table')
    
    if table:
        # Iterate over each row in the table body
        for row in table.tbody.find_all('tr'):
            # The first cell in each row contains the athlete's name
            name_cell = row.find('td')
            if name_cell:
                athlete_name = name_cell.get_text(strip=True)
                athlete_names.append(athlete_name)
    else:
        print("Table not found.")
else:
    print("'Recurve - Men' section not found.")

# Output the extracted athlete names
for name in athlete_names:
    print(name)