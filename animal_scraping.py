import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://test-scrape-site.onrender.com/animals.html"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

animals = soup.find_all('div', class_='animal-card')

data = []

for card in animals:
    name = card.find('h2')
    fact = card.find('p', class_='fact')
    habitat = card.find('p', class_='habitat')
    lifespan = card.find('p', class_='lifespan')
    diet = card.find('p', class_='diet')

    data.append([
        name.text.strip(),
        fact.text.strip(),
        habitat.text.replace("Habitat:", "").strip(),
        lifespan.text.replace("Lifespan:", "").strip(),
        diet.text.replace("Diet:", "").strip()
    ])

wb = Workbook()
ws = wb.active
ws.title = "Animal Data"

headers = ['Name', 'Fact', 'Habitat', 'Lifespan', 'Diet']
ws.append(headers)

for row in data:
    ws.append(row)

excel_filename = 'Animals_Data.xlsx'
wb.save(excel_filename)
print(f"Data saved to {excel_filename}")