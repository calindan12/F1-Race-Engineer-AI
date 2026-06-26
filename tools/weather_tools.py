from langchain_core.tools import tool
import requests


@tool
def get_weather(session_key: int) -> dict:
    """
    Returns the weather conditions for a Formula 1 session.
    Use this tool when the user asks about weather, track conditions,
    temperature, rainfall, or how weather affected a race or qualifying session.
    """

    weather = requests.get(
        "https://api.openf1.org/v1/weather",
        params={
            "session_key": session_key,
        }
    ).json()

    if not isinstance(weather, list):
        return {
            "error": weather.get("detail", "Unknown error")
        }

    if not weather:
        return {
            "error": "No weather data found."
        }

    return {
        "weather": weather
    }