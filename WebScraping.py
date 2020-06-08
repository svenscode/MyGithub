import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.XsVSUy_36u4')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
week = soup.find(id="seven-day-forecast-body")
#print(week)
#print(week.find_all('li'))
items = week.find_all(class_='tombstone-container')
# print(items[0])
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
#print(period_names)
short_desc = [item.find(class_='short-desc').get_text() for item in items]
#print(short_desc)
temp = [item.find(class_='temp').get_text() for item in items]
#print(temp)

weather_stuff = pd.DataFrame({
    'period': period_names,
    'short_desc': short_desc,
    'temp': temp,
})
print(weather_stuff)

weather_stuff.to_csv('weather.csv')


