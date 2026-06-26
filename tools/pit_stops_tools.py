from langchain_core.tools import tool
import requests


@tool
def get_pit_stops(driver_number: int, session_key: int) -> dict:
    """
    Returns all pit stops completed by a Formula 1 driver.

    Use this tool when the user asks about pit strategy,
    pit stop timing or pit stop duration.
    """

    response = requests.get(
        "https://api.openf1.org/v1/pit",
        params={
            "session_key": session_key,
            "driver_number": driver_number
        }
    )

    pitstops = response.json()

    if not isinstance(pitstops, list):
        return {
            "error": pitstops.get("detail", "Unknown error")
        }

    if not pitstops:
        return {
            "error": "No pit stop data found."
        }

    result = []

    for stop in pitstops:
        result.append(
            {
                "lap_number": stop["lap_number"],
                "pit_duration": stop["pit_duration"]
            }
        )

    return {
        "driver_number": driver_number,
        "session_key": session_key,
        "pit_stops": result
    }