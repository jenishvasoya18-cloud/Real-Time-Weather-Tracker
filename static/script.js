// ========================================
// DOM ELEMENTS
// ========================================

const cityInput =
    document.getElementById("cityInput");

const searchButton =
    document.getElementById("searchButton");

const clearButton =
    document.getElementById("clearButton");


// ========================================
// GET WEATHER
// ========================================

async function getWeather() {

    const errorDiv =
        document.getElementById("error");

    const city =
        cityInput.value.trim();


    // -----------------------------
    // Validate input
    // -----------------------------

    if (!city) {

        showError(
            "Please enter a city name."
        );

        cityInput.focus();

        return;
    }


    hideError();


    // -----------------------------
    // Loading state
    // -----------------------------

    setLoading(true);


    try {

        const response =
            await fetch(
                `/weather?city=${encodeURIComponent(city)}`
            );


        const data =
            await response.json();


        console.log(
            "Weather Data:",
            data
        );


        // -----------------------------
        // Backend error
        // -----------------------------

        if (!response.ok) {

            throw new Error(
                data.error ||
                "Unable to get weather data."
            );
        }


        // -----------------------------
        // Update background
        // -----------------------------

        updateWeatherBackground(
            data.weather
        );


        // -----------------------------
        // Main information
        // -----------------------------

        document.getElementById(
            "city"
        ).textContent =
            data.city || "--";


        document.getElementById(
            "country"
        ).textContent =
            getCountryFlag(
                data.country
            );


        document.getElementById(
            "countryCard"
        ).textContent =
            getCountryName(
                data.country
            );


        document.getElementById(
            "temperature"
        ).textContent =
            `${formatNumber(
                data.temperature
            )}°C`;


        document.getElementById(
            "condition"
        ).textContent =
            data.description || "--";


        // -----------------------------
        // Weather icon
        // -----------------------------

        updateWeatherIcon(
            data.icon,
            data.description
        );


        // -----------------------------
        // Weather details
        // -----------------------------

        document.getElementById(
            "feels"
        ).textContent =
            `${formatNumber(
                data.feels_like
            )}°C`;


        document.getElementById(
            "humidity"
        ).textContent =
            `${data.humidity ?? "--"}%`;


        document.getElementById(
            "wind"
        ).textContent =
            `${formatNumber(
                data.wind_speed
            )} m/s`;


        document.getElementById(
            "direction"
        ).textContent =
            getWindDirection(
                data.wind_direction
            );


        // -----------------------------
        // Information cards
        // -----------------------------

        document.getElementById(
            "clouds"
        ).textContent =
            `${data.clouds ?? "--"}%`;


        document.getElementById(
            "visibility"
        ).textContent =
            `${formatNumber(
                data.visibility
            )} km`;


        // -----------------------------
        // Sunrise / Sunset
        // -----------------------------

        document.getElementById(
            "sunrise"
        ).textContent =
            formatTime(
                data.sunrise,
                data.timezone
            );


        document.getElementById(
            "sunset"
        ).textContent =
            formatTime(
                data.sunset,
                data.timezone
            );


        // -----------------------------
        // Last updated
        // -----------------------------

        document.getElementById(
            "updatedTime"
        ).textContent =
            new Date().toLocaleTimeString(
                [],
                {
                    hour: "2-digit",
                    minute: "2-digit",
                    second: "2-digit"
                }
            );


    } catch (error) {

        console.error(
            "Weather Error:",
            error
        );


        showError(
            error.message ||
            "Something went wrong."
        );


    } finally {

        setLoading(false);
    }
}


// ========================================
// WEATHER BACKGROUND
// ========================================

function updateWeatherBackground(
    weather
) {

    const weatherType =
        (weather || "clouds")
        .toLowerCase();


    const validTypes = [
        "clear",
        "clouds",
        "rain",
        "drizzle",
        "thunderstorm",
        "snow",
        "mist",
        "smoke",
        "haze",
        "dust",
        "fog",
        "sand",
        "ash",
        "squall",
        "tornado"
    ];


    document.body.classList.remove(
        ...validTypes.map(
            type => `weather-${type}`
        )
    );


    if (
        validTypes.includes(
            weatherType
        )
    ) {

        document.body.classList.add(
            `weather-${weatherType}`
        );

    } else {

        document.body.classList.add(
            "weather-clouds"
        );
    }
}


// ========================================
// WEATHER ICON
// ========================================

function updateWeatherIcon(
    iconCode,
    description
) {

    const weatherIcon =
        document.getElementById(
            "weatherIcon"
        );


    if (!weatherIcon) {
        return;
    }


    const code =
        iconCode || "01d";


    weatherIcon.src =
        `https://openweathermap.org/img/wn/${code}@4x.png`;


    weatherIcon.alt =
        description || "Weather";
}


// ========================================
// WIND DIRECTION
// ========================================

function getWindDirection(
    degree
) {

    if (
        degree === undefined ||
        degree === null ||
        isNaN(Number(degree))
    ) {
        return "--";
    }


    const directions = [
        "N",
        "NE",
        "E",
        "SE",
        "S",
        "SW",
        "W",
        "NW"
    ];


    const index =
        Math.round(
            Number(degree) / 45
        ) % 8;


    return directions[index];
}


// ========================================
// TIME FORMAT
// ========================================

function formatTime(
    timestamp,
    timezoneOffset
) {

    if (!timestamp) {
        return "--";
    }


    const offset =
        Number(timezoneOffset) || 0;


    const date =
        new Date(
            (Number(timestamp) + offset)
            * 1000
        );


    return date.toLocaleTimeString(
        "en-IN",
        {
            timeZone: "UTC",
            hour: "2-digit",
            minute: "2-digit",
            hour12: true
        }
    );
}


// ========================================
// NUMBER FORMAT
// ========================================

function formatNumber(
    value
) {

    if (
        value === undefined ||
        value === null ||
        isNaN(Number(value))
    ) {
        return "--";
    }


    return Number(value).toFixed(1);
}


// ========================================
// COUNTRY FLAG
// ========================================

function getCountryFlag(
    countryCode
) {

    if (!countryCode) {
        return "--";
    }


    const code =
        countryCode.toUpperCase();


    if (code.length !== 2) {
        return code;
    }


    const flag =
        String.fromCodePoint(
            ...[...code].map(
                char =>
                    127397 +
                    char.charCodeAt(0)
            )
        );


    return `${flag} ${code}`;
}


// ========================================
// COUNTRY NAME
// ========================================

function getCountryName(
    countryCode
) {

    const countries = {

        IN: "India",

        US: "United States",

        GB: "United Kingdom",

        CA: "Canada",

        AU: "Australia",

        AE: "United Arab Emirates",

        SG: "Singapore",

        JP: "Japan",

        CN: "China",

        DE: "Germany",

        FR: "France",

        IT: "Italy",

        ES: "Spain",

        NZ: "New Zealand",

        BR: "Brazil",

        ZA: "South Africa"

    };


    return countries[
        countryCode?.toUpperCase()
    ] || countryCode || "--";
}


// ========================================
// LOADING STATE
// ========================================

function setLoading(
    loading
) {

    if (!searchButton) {
        return;
    }


    searchButton.disabled =
        loading;


    if (loading) {

        searchButton.innerHTML =
            `
            <span class="search-icon">
                ⏳
            </span>
            <span>
                Searching...
            </span>
            `;

    } else {

        searchButton.innerHTML =
            `
            <span class="search-icon">
                🔍
            </span>
            <span>
                Search
            </span>
            `;
    }
}


// ========================================
// ERROR
// ========================================

function showError(
    message
) {

    const errorDiv =
        document.getElementById(
            "error"
        );


    errorDiv.textContent =
        message;


    errorDiv.style.display =
        "block";
}


function hideError() {

    const errorDiv =
        document.getElementById(
            "error"
        );


    errorDiv.textContent =
        "";


    errorDiv.style.display =
        "none";
}


// ========================================
// CLEAR SEARCH
// ========================================

if (clearButton) {

    clearButton.addEventListener(
        "click",
        function () {

            cityInput.value = "";

            cityInput.focus();

            hideError();
        }
    );
}


// ========================================
// SEARCH BUTTON
// ========================================

if (searchButton) {

    searchButton.addEventListener(
        "click",
        getWeather
    );
}


// ========================================
// ENTER KEY
// ========================================

if (cityInput) {

    cityInput.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Enter"
            ) {

                event.preventDefault();

                getWeather();
            }
        }
    );
}


// ========================================
// INITIAL LOAD
// ========================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        getWeather();
    }
);