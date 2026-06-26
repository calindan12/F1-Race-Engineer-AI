from langchain_core.tools import tool
import requests


@tool
def get_lap_times(driver_number: int, session_key: int) -> dict:
    """
    Returns all lap times completed by a Formula 1 driver during a session.

    Use this tool when the user asks about:
    - lap times
    - race pace
    - fastest laps
    - consistency
    - performance over the course of a session.
    """

    response = requests.get(
        "https://api.openf1.org/v1/laps",
        params={
            "session_key": session_key,
            "driver_number": driver_number
        }
    )

    laps = response.json()

    if not isinstance(laps, list):
        return {
            "error": laps.get("detail", "Unknown error")
        }

    if not laps:
        return {
            "error": f"No lap data found for driver {driver_number}."
        }

    performance = []

    for lap in laps:
        performance.append(
            {
                "lap_number": lap["lap_number"],
                "lap_duration": lap["lap_duration"],
                "is_pit_out_lap": lap["is_pit_out_lap"],
                "segments_sector_1": lap["duration_sector_1"],
                "segments_sector_2": lap["duration_sector_2"],
                "segments_sector_3": lap["duration_sector_3"]
            }
        )

    return {
        "driver_number": driver_number,
        "session_key": session_key,
        "laps": performance
    }