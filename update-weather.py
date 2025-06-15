import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Kolkata"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

response = requests.get(URL)
data = response.json()

temp_c = data['current']['temp_c']
condition = data['current']['condition']['text']
icon = data['current']['condition']['icon']

weather_block = f"![icon](https:{icon}) **{CITY}**: {temp_c}°C, {condition}"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_tag = "<!-- WEATHER-START -->"
end_tag = "<!-- WEATHER-END -->"

start = content.find(start_tag)
end = content.find(end_tag)

if start != -1 and end != -1:
    new_content = content[:start + len(start_tag)] + "\n" + weather_block + "\n" + content[end:]
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
