import os
from datetime import datetime

import psycopg2
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# ==============================
# Database Connection
# ==============================

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


# ==============================
# Create Table
# ==============================

def create_table():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_history (
                id SERIAL PRIMARY KEY,
                city VARCHAR(100),
                country VARCHAR(50),
                temperature FLOAT,
                humidity INT,
                weather VARCHAR(100),
                searched_at TIMESTAMP
            );
        """)

        conn.commit()

        cur.close()
        conn.close()

        print("Database initialized successfully.")

    except Exception as e:
        print("Database Error:", e)


# ==============================
# Health Check
# ==============================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "Weather Backend API"
    }), 200


# ==============================
# Weather API
# ==============================

@app.route("/weather", methods=["GET"])
def weather():

    city = request.args.get("city")

    if not city:
        return jsonify({
            "error": "City parameter is required."
        }), 400

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return jsonify(response.json()), response.status_code

        data = response.json()

        result = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }

        # Save search history
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO weather_history
            (city, country, temperature, humidity, weather, searched_at)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                result["city"],
                result["country"],
                result["temperature"],
                result["humidity"],
                result["weather"],
                datetime.now()
            )
        )

        conn.commit()

        cur.close()
        conn.close()

        return jsonify(result), 200

    except requests.exceptions.RequestException:

        return jsonify({
            "error": "Unable to connect to OpenWeather API."
        }), 500

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==============================
# Search History
# ==============================

@app.route("/history", methods=["GET"])
def history():

    try:

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT city,
                   country,
                   temperature,
                   humidity,
                   weather,
                   searched_at
            FROM weather_history
            ORDER BY searched_at DESC
            LIMIT 10;
        """)

        rows = cur.fetchall()

        history = []

        for row in rows:
            history.append({
                "city": row[0],
                "country": row[1],
                "temperature": row[2],
                "humidity": row[3],
                "weather": row[4],
                "searched_at": row[5]
            })

        cur.close()
        conn.close()

        return jsonify(history), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==============================
# Main
# ==============================

if __name__ == "__main__":
    create_table()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
