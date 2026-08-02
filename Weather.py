import requests
from datetime import datetime
from config import API_KEY


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)

    return response.json()


def display_weather(data):

    if str(data.get("cod")) != "200":
        print("\n❌ City Not Found!")
        return

    city = data["name"]
    country = data["sys"]["country"]

    temperature = round(data["main"]["temp"] - 273.15, 2)
    feels_like = round(data["main"]["feels_like"] - 273.15, 2)

    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["main"]
    wind_speed = data["wind"]["speed"]

    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])

    print("\n========== WEATHER REPORT ==========")
    print(f"🌍 City         : {city}")
    print(f"🏳 Country      : {country}")
    print(f"🌡 Temperature  : {temperature} °C")
    print(f"🤗 Feels Like   : {feels_like} °C")
    print(f"💧 Humidity     : {humidity}%")
    print(f"☁ Weather      : {weather}")
    print(f"💨 Wind Speed   : {wind_speed} m/s")
    print(f"🌅 Sunrise      : {sunrise.strftime('%H:%M:%S')}")
    print(f"🌇 Sunset       : {sunset.strftime('%H:%M:%S')}")
    print("====================================")