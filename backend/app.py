from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "🌦️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 622:
        return "❄️"
    elif 701 <= weather_id <= 741:
        return "🌫️"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪️"
    elif weather_id == 800:
        return "☀️"
    elif 801 <= weather_id <= 804:
        return "☁️"
    else:
        return "🌍"

@app.route("/")
def home():
    return "Weather API running"


@app.route("/weather/<city>")
def weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    weather_id = data["weather"][0]["id"]
    result = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "emoji": get_weather_emoji(weather_id)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)