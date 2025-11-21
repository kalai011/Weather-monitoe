import requests

def get_weather(city):
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("❌ Error:", data.get("message", "Invalid city name"))
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]

        print("\n====== WEATHER REPORT ======")
        print(f"City      : {city}, {country}")
        print(f"Condition : {weather}")
        print(f"Temp      : {temp}°C (Feels like {feels_like}°C)")
        print(f"Min–Max   : {temp_min}°C / {temp_max}°C")
        print(f"Humidity  : {humidity}%")
        print(f"Wind Speed: {wind} m/s")
        print("============================\n")

    except Exception as e:
        print("⚠️ An error occurred:", str(e))


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
