import requests

API_KEY = "96d632c6ede623350f0a4c2d45c589e3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
recent_searches = []

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("City not found!")
            return

        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
        print("-" * 30)

        # Save to recent searches
        recent_searches.append(city)

    except requests.RequestException as e:
        print("Error fetching data:", e)

def show_recent_searches():
    if recent_searches:
        print("\nRecent Searches:")
        for city in recent_searches[-5:]:  # Show last 5 searches
            print(f"- {city}")
        print("-" * 30)
    else:
        print("\nNo recent searches yet.\n")

# App loop
while True:
    show_recent_searches()
    city = input("Enter city name (or 'exit' to quit): ").strip()

    if city.lower() == "exit":
        print("Goodbye!")
        break

    if city:
        get_weather(city)
