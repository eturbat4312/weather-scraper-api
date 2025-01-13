import requests
from bs4 import BeautifulSoup

# URL of the weather page
url = "https://www.accuweather.com/en/gb/london/ec4a-2/weather-forecast/328328"

# Mimic a browser with headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the temperature element
temperature_element = soup.find("div", class_="temp")
if temperature_element:
    temperature = temperature_element.text.strip()  # Extract and clean the text
else:
    temperature = "Not Found"

print("Temperature:", temperature)
