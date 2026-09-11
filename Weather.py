import requests
from datetime import datetime, timezone

from config import API_KEY


def get_weather(city):

    city = city.strip()


    if not city:

        raise ValueError(
            "City name cannot be empty."
        )


    url = (
        "https://api.openweathermap.org/"
        "data/2.5/weather"
    )


    params = {

        "q": city,

        "appid": API_KEY,

        "units": "metric"
    }


    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )


        try:

            data = response.json()

        except ValueError:

            raise Exception(
                "Invalid response from weather service."
            )


    except requests.exceptions.Timeout:

        raise Exception(
            "Weather service is taking too long to respond."
        )


    except requests.exceptions.ConnectionError:

        raise Exception(
            "Unable to connect to weather service."
        )


    except requests.exceptions.RequestException as e:

        raise Exception(
            f"Weather service error: {e}"
        )


    if response.status_code != 200:

        message = data.get(
            "message",
            "City not found."
        )

        raise Exception(
            message.capitalize()
        )


    return data


def display_weather(data):

    city = data["name"]

    country = data["sys"]["country"]


    temperature = data["main"]["temp"]

    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]


    weather = data["weather"][0]["main"]

    description = data["weather"][0][
        "description"
    ]


    wind_speed = data["wind"]["speed"]

    wind_direction = data["wind"].get(
        "deg",
        0
    )


    clouds = data["clouds"]["all"]


    visibility = data.get(
        "visibility",
        0
    ) / 1000


    timezone_offset = data.get(
        "timezone",
        0
    )


    # --------------------------------
    # Convert timestamp to city time
    # --------------------------------

    def city_time(timestamp):

        if not timestamp:
            return "--"


        utc_time = datetime.fromtimestamp(
            timestamp,
            tz=timezone.utc
        )


        adjusted_timestamp = (
            utc_time.timestamp()
            + timezone_offset
        )


        return datetime.fromtimestamp(
            adjusted_timestamp,
            tz=timezone.utc
        ).strftime(
            "%H:%M:%S"
        )


    sunrise = city_time(
        data["sys"]["sunrise"]
    )


    sunset = city_time(
        data["sys"]["sunset"]
    )


    # --------------------------------
    # Display
    # --------------------------------

    print(
        "\n===================================="
    )

    print(
        "         WEATHER REPORT"
    )

    print(
        "===================================="
    )


    print(
        f"🌍 City          : {city}"
    )


    print(
        f"🏳 Country       : {country}"
    )


    print(
        f"🌡 Temperature   : "
        f"{temperature:.1f} °C"
    )


    print(
        f"🤗 Feels Like    : "
        f"{feels_like:.1f} °C"
    )


    print(
        f"💧 Humidity      : "
        f"{humidity}%"
    )


    print(
        f"☁ Weather       : "
        f"{weather}"
    )


    print(
        f"📝 Description   : "
        f"{description.title()}"
    )


    print(
        f"💨 Wind Speed    : "
        f"{wind_speed:.1f} m/s"
    )


    print(
        f"🧭 Wind Direction: "
        f"{wind_direction}°"
    )


    print(
        f"☁ Clouds        : "
        f"{clouds}%"
    )


    print(
        f"👁 Visibility    : "
        f"{visibility:.1f} km"
    )


    print(
        f"🌅 Sunrise       : "
        f"{sunrise}"
    )


    print(
        f"🌇 Sunset        : "
        f"{sunset}"
    )


    print(
        "===================================="
    )