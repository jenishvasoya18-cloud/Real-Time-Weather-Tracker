from flask import Flask, render_template, request, jsonify
import requests
from config import API_KEY

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather():

    city = request.args.get("city", "").strip()

    # -----------------------------
    # Validate city
    # -----------------------------

    if not city:
        return jsonify({
            "error": "Please enter a city name."
        }), 400


    url = "https://api.openweathermap.org/data/2.5/weather"

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


        # Try to parse JSON
        try:
            data = response.json()

        except ValueError:

            return jsonify({
                "error": "Invalid response from weather service."
            }), 502


        # -----------------------------
        # OpenWeather error
        # -----------------------------

        if response.status_code != 200:

            return jsonify({
                "error": data.get(
                    "message",
                    "City not found."
                )
            }), response.status_code


        # -----------------------------
        # Weather information
        # -----------------------------

        weather_info = data.get(
            "weather",
            [{}]
        )[0]


        main_data = data.get(
            "main",
            {}
        )


        wind_data = data.get(
            "wind",
            {}
        )


        clouds_data = data.get(
            "clouds",
            {}
        )


        sys_data = data.get(
            "sys",
            {}
        )


        weather_data = {

            "city": data.get(
                "name",
                "--"
            ),

            "country": sys_data.get(
                "country",
                "--"
            ),

            "temperature": main_data.get(
                "temp"
            ),

            "feels_like": main_data.get(
                "feels_like"
            ),

            "description": weather_info.get(
                "description",
                "Unknown"
            ).title(),

            "weather": weather_info.get(
                "main",
                "Unknown"
            ),

            # OpenWeather icon code
            "icon": weather_info.get(
                "icon",
                "01d"
            ),

            "humidity": main_data.get(
                "humidity",
                0
            ),

            "wind_speed": wind_data.get(
                "speed",
                0
            ),

            "wind_direction": wind_data.get(
                "deg",
                0
            ),

            "clouds": clouds_data.get(
                "all",
                0
            ),

            "visibility": round(
                data.get(
                    "visibility",
                    0
                ) / 1000,
                1
            ),

            "sunrise": sys_data.get(
                "sunrise"
            ),

            "sunset": sys_data.get(
                "sunset"
            ),

            # City timezone offset in seconds
            "timezone": data.get(
                "timezone",
                0
            )
        }


        return jsonify(weather_data)


    except requests.exceptions.Timeout:

        return jsonify({
            "error":
                "Weather service is taking too long to respond."
        }), 504


    except requests.exceptions.ConnectionError:

        return jsonify({
            "error":
                "Unable to connect to weather service."
        }), 503


    except requests.exceptions.RequestException as e:

        print(
            "Request Error:",
            e
        )

        return jsonify({
            "error":
                "Unable to connect to weather service."
        }), 500


    except Exception as e:

        print(
            "Unexpected Error:",
            e
        )

        return jsonify({
            "error":
                "Something went wrong."
        }), 500


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )