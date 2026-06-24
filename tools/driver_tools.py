from langchain_core.tools import tool
import requests


@tool
def get_driver_info(driver_name:str)-> dict:
    """Returns driver information"""
    response = requests.get(
        "https://api.openf1.org/v1/drivers?session_key=11307"
    )

    drivers = response.json()

    for driver in drivers:
        full_name = (
            f"{driver['first_name']} {driver['last_name']}"
        )

        if full_name.lower() == driver_name.lower():

            return {
                "full_name": full_name,
                "team_name": driver["team_name"],
                "driver_number": driver["driver_number"],
                "acronym": driver["name_acronym"]
            }
        

    return {"error":"Driver not found"}
        