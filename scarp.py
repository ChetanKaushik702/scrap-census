import requests
from bs4 import BeautifulSoup
import json

source = requests.get('http://www.citypopulation.de/en/india/haryana/').text
soup = BeautifulSoup(source, 'lxml')
rows = soup.find('table', id='ts').tbody.find_all('tr')
dict = {}
for row in rows:
    city = row.find('td', class_='rname').a.text
    district = row.find('td', class_='radm rarea').text
    if district in dict and district != city:
        val = dict[district]
        val.append(city)
        dict[district] = val
    elif district != city:
        val = [city]
        dict[district] = val

# saving data into json file
with open('towns.json', 'w') as outfile:
    json.dump(dict, outfile)