from langchain_core.tools import tool
import requests

@tool
def get_team_info(team_name:str , session_key:int)->dict:
    """Returns information about an F1 team and the drivers of the team"""
    response = requests.get(
        "https://api.openf1.org/v1/drivers",
        params={
            "session_key": session_key
        }
    )

    drivers = response.json()
    team_drivers = []

    for driver in drivers:
        if team_name.lower() in driver["team_name"].lower():
            team_drivers.append(
                {
                    "full_name": f"{driver['first_name']} {driver['last_name']}",
                    "driver_number": driver["driver_number"],
                    "acronym": driver["name_acronym"]
                }
            )
    return {
        "team":team_name,
        "drivers":team_drivers
    }