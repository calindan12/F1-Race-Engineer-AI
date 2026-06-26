from langchain_core.tools import tool
import requests


@tool
def get_position_history(driver_number: int, session_key: int) -> dict:
    """
    Returns the position history of a Formula 1 driver during a session.

    Use this tool when the user asks how a driver's position evolved,
    when they gained or lost positions, or about overtakes during a session.
    """

    response = requests.get(
        "https://api.openf1.org/v1/position",
        params={
            "session_key": session_key,
            "driver_number": driver_number
        }
    )

    positions = response.json()

    if not isinstance(positions, list):
        return {
            "error": positions.get("detail", "Unknown error")
        }

    if not positions:
        return {
            "error": "No position history found."
        }

    history = []

    for position in positions:
        history.append(
            {
                "date": position["date"],
                "position": position["position"]
            }
        )

    return {
        "driver_number": driver_number,
        "session_key": session_key,
        "positions": history
    }