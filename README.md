# 🌦 Real-Time Weather Tracker

A simple and responsive **Real-Time Weather Tracker** built with **Python, Flask, JavaScript, HTML, and CSS**.

The application uses the **OpenWeather API** to retrieve real-time weather information for any city entered by the user.

---

## 📌 Features

* 🌍 Search weather by city name
* 🌡️ Current temperature in Celsius
* 🤗 Feels-like temperature
* 💧 Humidity percentage
* 💨 Wind speed
* 🧭 Wind direction
* ☁️ Cloud coverage
* 👁️ Visibility
* 🌅 Sunrise time
* 🌇 Sunset time
* 🏳️ Country information
* 🌤️ Dynamic weather icons
* 🔄 Last updated time
* ⌨️ Press **Enter** to search
* 📱 Responsive design for desktop, tablet, and mobile
* ⚠️ User-friendly error messages
* ⏳ Loading state while fetching weather data
* 🖥️ Includes both a web interface and command-line interface

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* Requests

### Frontend

* HTML5
* CSS3
* JavaScript

### API

* OpenWeather API

---

## 📂 Project Structure

```text
Weather-App/
│
├── app.py
├── main.py
├── weather.py
├── config.py
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ Requirements

Make sure you have the following installed:

* Python 3.9 or higher
* pip
* An OpenWeather API key

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
```

Move into the project directory:

```bash
cd weather-app
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install flask requests
```

---

## 🔑 OpenWeather API Setup

This application requires an API key from OpenWeather.

Create an account and generate an API key.

Do **not** publish your API key on GitHub or share it publicly.

Add your API key to `config.py`:

```python
API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

### ⚠️ Security

Never commit your real API key to a public repository.

Add `config.py` to `.gitignore`:

```text
config.py
```

If an API key has already been pushed to GitHub, revoke it and generate a new one.

---

# 🌐 Running the Web Application

Start the Flask application:

```bash
python app.py
```

You should see something similar to:

```text
 * Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The Weather Tracker interface will appear.

---

# 🖥️ Running the Command-Line Application

The project also includes a command-line version.

Run:

```bash
python main.py
```

You will be asked to enter a city:

```text
🌦 Welcome to Weather App

Enter City Name: Ahmedabad
```

The application will display a weather report containing information such as:

```text
====================================
         WEATHER REPORT
====================================
🌍 City         : Ahmedabad
🏳 Country      : IN
🌡 Temperature  : 30.5 °C
🤗 Feels Like   : 32.1 °C
💧 Humidity     : 65%
☁ Weather      : Clouds
📝 Description  : Broken Clouds
💨 Wind Speed   : 3.2 m/s
🧭 Wind Direction: 270°
☁ Clouds       : 75%
👁 Visibility   : 10.0 km
🌅 Sunrise      : 06:15:20
🌇 Sunset       : 18:45:10
====================================
```

You can search for another city by entering:

```text
y
```

or exit by entering:

```text
n
```

---

# 🔄 How the Application Works

The application follows this flow:

```text
User enters city
        ↓
Frontend sends request
        ↓
Flask /weather endpoint
        ↓
OpenWeather API
        ↓
Weather data received
        ↓
Flask processes the response
        ↓
JSON returned to frontend
        ↓
JavaScript updates the UI
```

---

# 🔌 API Endpoint

The Flask application provides the following endpoint:

```text
GET /weather?city={city_name}
```

### Example

```text
/weather?city=Ahmedabad
```

The endpoint returns weather information in JSON format.

Example:

```json
{
    "city": "Ahmedabad",
    "country": "IN",
    "temperature": 30.5,
    "feels_like": 32.1,
    "description": "Broken Clouds",
    "weather": "Clouds",
    "humidity": 65,
    "wind_speed": 3.2,
    "wind_direction": 270,
    "clouds": 75,
    "visibility": 10.0,
    "sunrise": 1757468710,
    "sunset": 1757514630,
    "timezone": 19800
}
```

---

# 🧩 Main Files

## `app.py`

The Flask backend.

Responsibilities:

* Creates the Flask application
* Serves the HTML page
* Receives city search requests
* Calls OpenWeather API
* Processes weather data
* Returns JSON responses
* Handles API and connection errors

---

## `weather.py`

Contains the reusable weather API functions.

Main functions:

```python
get_weather(city)
```

Retrieves weather information from OpenWeather.

```python
display_weather(data)
```

Displays weather information in the terminal.

---

## `main.py`

Runs the command-line version of the application.

It allows the user to:

* Enter a city
* View weather information
* Search another city
* Exit the application

---

## `templates/index.html`

Contains the structure of the web application.

It includes:

* Header
* Search box
* Weather card
* Weather details
* Information cards
* Last updated section

---

## `static/style.css`

Contains the complete styling of the application.

It provides:

* Weather dashboard design
* Responsive layout
* Glassmorphism weather card
* Search interface
* Mobile responsiveness
* Tablet responsiveness
* Hover effects
* Error message styling

---

## `static/script.js`

Handles frontend functionality.

Responsibilities:

* Sends weather requests
* Updates weather information
* Displays weather icons
* Converts wind degrees to directions
* Formats sunrise and sunset
* Handles errors
* Displays loading status
* Supports Enter-key search

---

## 🛡️ Error Handling

The application handles several common errors.

### Empty city

```text
Please enter a city name.
```

### Invalid city

```text
City not found.
```

### Internet connection problem

```text
Unable to connect to weather service.
```

### API timeout

```text
Weather service is taking too long to respond.
```

### Unexpected server error

```text
Something went wrong.
```

---

# 📱 Responsive Design

The application is designed to work on:

* 🖥️ Desktop
* 💻 Laptop
* 📱 Mobile
* 📟 Tablet

The layout automatically adjusts according to screen size using CSS media queries.

---

# 🌤️ Supported Weather Conditions

The application displays different icons for conditions such as:

* Clear ☀️
* Clouds ☁️
* Rain 🌧️
* Drizzle 🌦️
* Thunderstorm ⛈️
* Snow ❄️
* Mist 🌫️
* Smoke 🌫️
* Haze 🌫️
* Dust 🌪️
* Fog 🌫️
* Sand 🌪️
* Ash 🌋
* Squall 💨
* Tornado 🌪️

---

# 🔐 Recommended `.gitignore`

Create a `.gitignore` file in the project root:

```text
venv/
.venv/
__pycache__/
*.pyc
config.py
.env
```

This prevents sensitive configuration files and Python-generated files from being uploaded to GitHub.

---

# 🐛 Troubleshooting

## Flask command not found

Install Flask:

```bash
pip install flask
```

---

## Requests module not found

Install Requests:

```bash
pip install requests
```

---

## API key error

Check that your `config.py` contains a valid OpenWeather API key:

```python
API_KEY = "YOUR_API_KEY"
```

---

## City not found

Try entering the city name again.

Examples:

```text
Ahmedabad
Mumbai
Delhi
Rajkot
London
New York
Tokyo
```

---

## Port already in use

If port `5000` is already being used, change the port in `app.py`:

```python
app.run(
    debug=True,
    host="127.0.0.1",
    port=5001
)
```

Then open:

```text
http://127.0.0.1:5001
```

---

# 🚀 Future Improvements

Possible future enhancements include:

* 📍 Detect weather using the user's location
* 📅 5-day weather forecast
* 🌡️ Hourly weather forecast
* 🌙 Dark/light weather themes
* 🌧️ Rain probability
* 🌬️ Air Quality Index
* 🌎 Multiple saved cities
* ⭐ Favorite cities
* 📊 Weather charts
* 🌡️ Celsius/Fahrenheit switch
* 🗺️ Weather map
* 🔔 Severe weather alerts
* 📱 Progressive Web App support
* 🔐 Store API key using environment variables
* ☁️ Deploy the application online

---

# 📄 License

This project is created for learning and demonstration purposes.

You are free to modify and improve the project for your own use.

---

# 👨‍💻 Author

**Jenish Vasoya**

Weather Tracker built using:

**Python + Flask + JavaScript + OpenWeather API**

---

## ⭐ If you like this project

If this project helped you learn Flask, APIs, JavaScript, or frontend development, consider giving the repository a ⭐ on GitHub.
