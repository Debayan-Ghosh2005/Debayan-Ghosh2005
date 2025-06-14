import requests
from datetime import datetime

API_KEY = os.environ.get("WEATHER_API_KEY")
LOCATION = "Kolkata"

def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"
    response = requests.get(url)
    return response.json()

def update_readme(weather_data):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    icon_url = f"https:{weather_data['current']['condition']['icon']}"
    condition = weather_data['current']['condition']['text']
    temp_c = weather_data['current']['temp_c']
    date_str = datetime.now().strftime("%d/%m/%Y")

    weather_html = f"""
<h3 align="center">Today's Weather</h3>
<div align="center">
  <p>Kolkata, India - {date_str}</p>
  <img src="{icon_url}" />
  <p>{condition}, {temp_c}°C</p>
</div>
"""

    # Replace between these two tags
    start_tag = "<!-- WEATHER-START -->"
    end_tag = "<!-- WEATHER-END -->"
    start = content.find(start_tag)
    end = content.find(end_tag)

    if start != -1 and end != -1:
        new_content = content[:start + len(start_tag)] + weather_html + content[end:]
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)

weather_data = get_weather()
update_readme(weather_data)
