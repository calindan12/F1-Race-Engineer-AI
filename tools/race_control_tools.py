from langchain_core.tools import tool
import requests


@tool
def get_race_control(session_key: int) -> dict:
    """
    Returns all Race Control messages for a Formula 1 session.

    Use this tool when the user asks about Safety Cars,
    Virtual Safety Cars, Red Flags, Yellow Flags,
    penalties or race incidents.
    """

    response = requests.get(
        "https://api.openf1.org/v1/race_control",
        params={
            "session_key": session_key
        }
    )

    messages = response.json()

    if not isinstance(messages, list):
        return {
            "error": messages.get("detail", "Unknown error")
        }

    if not messages:
        return {
            "error": "No race control messages found."
        }

    result = []

    for message in messages:
        result.append(
            {
                "date": message["date"],
                "category": message["category"],
                "message": message["message"]
            }
        )

    return {
        "session_key": session_key,
        "messages": result
    }