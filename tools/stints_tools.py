from langchain_core.tools import tool
import requests


@tool
def get_stints(driver_number: int, session_key: int) -> dict:
    """
    Returns the tyre stints of a Formula 1 driver.

    Use this tool when the user asks about tyre strategy,
    compounds used, stint lengths or pit strategy.
    """

    response = requests.get(
        "https://api.openf1.org/v1/stints",
        params={
            "session_key": session_key,
            "driver_number": driver_number
        }
    )

    stints = response.json()

    if not isinstance(stints, list):
        return {
            "error": stints.get("detail", "Unknown error")
        }

    if not stints:
        return {
            "error": "No stint data found."
        }

    result = []

    for stint in stints:
        result.append(
            {
                "compound": stint["compound"],
                "lap_start": stint["lap_start"],
                "lap_end": stint["lap_end"],
                "tyre_age_at_start": stint["tyre_age_at_start"]
            }
        )

    return {
        "driver_number": driver_number,
        "session_key": session_key,
        "stints": result
    }