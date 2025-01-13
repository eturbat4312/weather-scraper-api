import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime


# Step 1: Scrape Weather Data
def scrape_weather():
    url = "https://www.accuweather.com/en/gb/london/ec4a-2/weather-forecast/328328"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    # Send a GET request to the weather page
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the temperature
    temperature_element = soup.find("div", class_="temp")
    if temperature_element:
        temperature = temperature_element.text.strip()  # Get the text and clean it
    else:
        temperature = "Not Found"

    # Placeholder for wind and rain if you decide to extract them later
    wind = "N/A"
    rain = "N/A"

    return temperature, wind, rain


# Step 2: Insert Data into MySQL
def insert_weather_data(temperature, wind, rain):
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="mysql",  # Docker service name for MySQL
        user="user",
        password="password",
        database="weather_db",
        port=3306,
    )
    cursor = db.cursor()

    # Create weather_data table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weather_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            temperature VARCHAR(10),
            wind VARCHAR(50),
            rain VARCHAR(50)
        )
    """
    )
    db.commit()

    # Insert the scraped weather data
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute(
        """
        INSERT INTO weather_data (date, temperature, wind, rain)
        VALUES (%s, %s, %s, %s)
    """,
        (date, temperature, wind, rain),
    )
    db.commit()

    print(f"Weather data inserted: {temperature}, {wind}, {rain}")

    # Close the database connection
    cursor.close()
    db.close()


# Main script execution
if __name__ == "__main__":
    # Step 1: Scrape the weather
    temperature, wind, rain = scrape_weather()
    print(f"Temperature: {temperature}, Wind: {wind}, Rain: {rain}")

    # Step 2: Insert into the database
    insert_weather_data(temperature, wind, rain)
