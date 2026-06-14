import requests

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_LOCATION = {"latitude": 34.0522, "longitude": -118.2437, "timezone": "auto"}

WEATHER_CODE_MAP = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def get_weather():
    response = requests.get(WEATHER_API_URL, params={**DEFAULT_LOCATION, "current_weather": True}, timeout=10)
    response.raise_for_status()
    data = response.json()
    current = data.get("current_weather", {})
    temperature = current.get("temperature")
    weather_code = current.get("weathercode")
    if temperature is None or weather_code is None:
        raise ValueError("Failed to parse weather response")
    condition = WEATHER_CODE_MAP.get(weather_code, "Unknown conditions")
    return f"{temperature} C", condition
