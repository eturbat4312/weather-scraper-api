# **Weather Scraper and API**

This project is a fully containerized weather scraping and REST API system. It scrapes weather data (temperature, wind, rain) from a reliable source and provides endpoints to retrieve the data stored in a MySQL database.

---

## **Features**

### **Daily Weather Scraper**

- Collects current weather data such as temperature, wind speed, and rain.
- Stores the scraped data into a MySQL database.

### **REST API**

- Fetch the latest weather data.
- Retrieve weather data by a specific date.
- Get multiple recent records.

### **Dockerized Environment**

- Runs the scraper, API, and MySQL services in separate Docker containers.

---

## **Project Structure**

```plaintext
weather_app/
├── api.py                 # Flask API to handle user requests
├── scraper.py             # Weather scraping script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Dockerfile for building the application image
├── docker-compose.yml     # Docker Compose configuration for the system
└── README.md              # Project documentation
```

---

## **Setup Instructions**

### **Prerequisites**

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### **Steps to Run**

1. Clone this repository:

2. Navigate to the project directory:

   ```bash
   cd weather-scraper-api
   ```

3. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

The API will be accessible at **http://localhost:5001**.

---

## **API Endpoints**

### **1. Get Latest Weather Data**

- **Endpoint**: `/weather`
- **Method**: `GET`
- **Description**: Returns the most recently scraped weather data.
- **Example Request**:
  ```bash
  curl http://localhost:5001/weather
  ```
- **Example Response**:
  ```json
  {
    "id": 1,
    "date": "2025-01-13",
    "temperature": "4°C",
    "wind": "N/A",
    "rain": "N/A"
  }
  ```

---

### **2. Get Weather Data by Date**

- **Endpoint**: `/weather_by_date`
- **Method**: `GET`
- **Description**: Returns weather data for a specific date.
- **Query Parameters**:
  - `date`: The date in `YYYY-MM-DD` format.
- **Example Request**:
  ```bash
  curl "http://localhost:5001/weather_by_date?date=2025-01-13"
  ```
- **Example Response**:
  ```json
  [
    {
      "id": 1,
      "date": "2025-01-13",
      "temperature": "4°C",
      "wind": "N/A",
      "rain": "N/A"
    }
  ]
  ```

---

### **3. Get Recent Weather Data**

- **Endpoint**: `/weather/recent`
- **Method**: `GET`
- **Description**: Fetches the most recent weather records.
- **Query Parameters**:
  - `limit`: Number of records to fetch (default: 10).
- **Example Request**:
  ```bash
  curl "http://localhost:5001/weather/recent?limit=5"
  ```
- **Example Response**:
  ```json
  [
    {
      "id": 3,
      "date": "2025-01-13",
      "temperature": "4°C",
      "wind": "N/A",
      "rain": "N/A"
    },
    {
      "id": 2,
      "date": "2025-01-12",
      "temperature": "5°C",
      "wind": "10 km/h",
      "rain": "2 mm"
    }
  ]
  ```

---

## **How It Works**

### **1. Scraper**

- The `scraper.py` script collects weather data from a specified website and stores it in the MySQL database.
- Runs automatically when the container starts.

### **2. API**

- The `api.py` script provides RESTful endpoints to retrieve weather data from the database.

---

## **Enhancements**

Here are potential improvements for the project:

- Add historical weather data scraping.
- Include forecast data.
- Implement API authentication and rate limiting.
- Automate periodic execution of the scraper using a scheduler like `cron` or `apscheduler`.

---
