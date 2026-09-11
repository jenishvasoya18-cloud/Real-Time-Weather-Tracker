from weather import (
    get_weather,
    display_weather
)


def main():

    print(
        "🌦 Welcome to Weather App"
    )


    while True:

        city = input(
            "\nEnter City Name: "
        ).strip()


        if not city:

            print(
                "❌ Please enter a city name."
            )

            continue


        try:

            data = get_weather(
                city
            )


            display_weather(
                data
            )


        except Exception as e:

            print(
                f"\n❌ Error: {e}"
            )


        choice = input(
            "\nDo you want to search "
            "another city? (y/n): "
        ).strip().lower()


        if choice != "y":

            print(
                "\n👋 Thank You for using "
                "Weather App!"
            )

            break


if __name__ == "__main__":

    main()