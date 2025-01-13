import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)


# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",  # Docker service name for MySQL
        user="user",
        password="password",
        database="weather_db",
        port=3306,
    )


# Endpoint to fetch the latest weather data
@app.route("/weather", methods=["GET"])
def get_latest_weather():
    try:
        # Connect to the database
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        # Fetch the latest weather data
        cursor.execute("SELECT * FROM weather_data ORDER BY id DESC LIMIT 1")
        data = cursor.fetchone()

        # Close the database connection
        cursor.close()
        db.close()

        if data:
            return jsonify(data)  # Return data as JSON
        else:
            return jsonify({"error": "No weather data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/weather_by_date", methods=["GET"])
def get_weather_by_date():
    try:
        # Get the date from the query parameters
        date = request.args.get("date")
        if not date:
            return jsonify({"error": "Please provide a date (YYYY-MM-DD)"}), 400

        # Connect to the database
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        # Query weather data for the specific date
        cursor.execute("SELECT * FROM weather_data WHERE date = %s", (date,))
        data = cursor.fetchall()

        # Close the database connection
        cursor.close()
        db.close()

        if data:
            return jsonify(data)  # Return all records for the date
        else:
            return (
                jsonify({"error": "No weather data found for the specified date"}),
                404,
            )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/weather/recent", methods=["GET"])
def get_recent_weather():
    try:
        # Get the limit from query parameters (default to 10 if not provided)
        limit = request.args.get("limit", 10)

        # Connect to the database
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        # Query the most recent weather data
        cursor.execute(
            "SELECT * FROM weather_data ORDER BY id DESC LIMIT %s", (int(limit),)
        )
        data = cursor.fetchall()

        # Close the database connection
        cursor.close()
        db.close()

        if data:
            return jsonify(data)  # Return the most recent records
        else:
            return jsonify({"error": "No weather data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
