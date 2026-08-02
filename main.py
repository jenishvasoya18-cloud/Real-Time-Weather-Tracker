from Weather import get_weather, display_weather

print("🌦 Welcome to Weather App")

while True:

    city = input("\nEnter City Name: ")

    try:

        data = get_weather(city)

        display_weather(data)

    except Exception as e:

        print("❌ Error:", e)

    choice = input("\nDo you want to search another city? (y/n): ")

    if choice.lower() != "y":
        print("\n👋 Thank You for using Weather App!")
        break