import requests

def get_temperature():
    try:
        url = "https://wttr.in/Gulbarga?format=j1"
        response = requests.get(url)
        data = response.json()

        if "current_condition" in data:
            current = data["current_condition"][0]
            temperature = current["temp_C"]
            feels_like = current["FeelsLikeC"]
            humidity = current["humidity"]
            weather_desc = current["weatherDesc"][0]["value"]

            reply = (
                f"🌡 Temperature in Gulbarga: {temperature}°C\n"
                f"🤗 Feels like: {feels_like}°C\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌤 Condition: {weather_desc}"
            )
            return reply
        else:
            return "❌ Failed to fetch weather data."

    except Exception as e:
        return f"⚠️ Exception occurred: {str(e)}"

