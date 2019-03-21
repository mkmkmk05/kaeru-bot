import requests
from bs4 import BeautifulSoup
 
url = "https://transit.yahoo.co.jp/search/result?from=%E5%A4%A7%E5%B4%8E&to=%E6%96%B0%E5%B7%9D%E5%B4%8E&y=2019&m=03&d=19&hh=15&m2=4&m1=1&type=1&ticket=ic&expkind=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1&kw=%E6%96%B0%E5%B7%9D%E5%B4%8E"
 
response = requests.get(url)
response.encoding = response.apparent_encoding
 
bs = BeautifulSoup(response.text, 'html.parser')
 
routes = bs.findAll('div', class_='routeDetail')
for route in routes:
    stations = route.findAll('div', reversed=False, class_='station')
#    stations = route.findAll('div', class_='station', reversed=False)
#    stations = route.select('div.station')
    for station in stations:
        tm = station.find('ul', class_='time')
        print(tm.getText())

