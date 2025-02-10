import requests
from bs4 import BeautifulSoup

# URL for Wikipedia page with the list of countries
url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

# Fetch and parse the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract country names from the table
countries = []
table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

for row in rows[1:]:
    if "static-row-numbers-norank" in row.get("class", []):
        continue
    cells = row.find_all('td')
    if cells:
        country_name = cells[0].text.strip()
        countries.append(country_name)

# Save to a file
with open("countries.txt", "w") as f:
    for country in countries:
        f.write(country + "\n")

print(f"Extracted {len(countries)} countries.")
