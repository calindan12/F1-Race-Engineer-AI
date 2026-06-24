from langchain_core.tools import tool
import requests

@tool
def get_team_info(team_name:str)->dict:
    """Returns information about an F1 team"""
    response = requests.get(
        "https://api.openf1.org/v1/drivers?session_key=11307"
    )

    drivers = response.json()
    team_drivers = []

    for driver in drivers:
        if driver["team_name"].lower() == team_name.lower():
            team_drivers.append(
                f"{driver['first_name']} {driver['last_name']}"
            )

        return {
            "team":team_name,
            "drivers":team_drivers
        }