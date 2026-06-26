from langchain_core.tools import tool
import requests

@tool
def get_session_context(country_name:str , session_name:str, year:int)->dict:
    """
    Returns the meeting_key and session_key for a Formula 1 session.

    Arguments:
    - country_name: the country where the Grand Prix took place.
    - session_name: must be exactly one of:
    - Race
    - Qualifying
    - Sprint
    - Sprint Qualifying
    - Practice 1
    - Practice 2
    - Practice 3
    - year: Formula 1 season.

    Do not pass the Grand Prix name as session_name.
    If the user does not specify the session type, use "Race".
    """
    response = requests.get(
        "https://api.openf1.org/v1/sessions",
        params={
            "country_name": country_name,
            "session_name": session_name,
            "year": year
        }
    )
    sessions = response.json()
    
    if not isinstance(sessions, list):
        return {
            "error": sessions.get("detail", "Unknown error")
        }

    if not sessions:
        return {
            "error": "No session found."
        }

    print(type(sessions))
    print(sessions)

    for session in sessions:
        if country_name.lower() in session["country_name"].lower() and session_name.lower() in session["session_name"].lower() and session["year"] == year:
            return {
                "meeting_key": session["meeting_key"],
                "session_key": session["session_key"],
                "country_name": session["country_name"],
                "circuit": session["circuit_short_name"],
                "session_name": session["session_name"],
                "year": session["year"]
            }