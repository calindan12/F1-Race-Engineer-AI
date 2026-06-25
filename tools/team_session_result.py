from langchain_core.tools import tool
import requests


@tool
def get_team_session_result(team_name: str, session_key: int) -> dict:
    """Returns the final performance and classification of all drivers
    from an F1 team in a specific session (Qualifying, Sprint, Race).
    Use this tool when the user asks how a team performed in a session."""

    drivers = requests.get(
        "https://api.openf1.org/v1/drivers",
        params={
            "session_key": session_key,
            "team_name": team_name
        }
    ).json()

    if not drivers:
        return {
            "error": f"No drivers found for team '{team_name}' in session {session_key}"
        }

    session_results = requests.get(
        "https://api.openf1.org/v1/session_result",
        params={
            "session_key": session_key
        }
    ).json()

    results_by_driver = {
        result["driver_number"]: result
        for result in session_results
    }

    performance = []

    for driver in drivers:

        driver_result = results_by_driver.get(driver["driver_number"])

        # print("driver_result: " , driver_result)

        if driver_result:

            qualifying_results = []

            durations = driver_result["duration"]
            gaps = driver_result["gap_to_leader"]

            for i in range(len(durations)):
                qualifying_results.append(
                    {
                        "session": f"Q{i + 1}",
                        "duration": durations[i],
                        "gap_to_leader": gaps[i]
                    }
                )

            performance.append(
                {
                    "driver": f"{driver['first_name']} {driver['last_name']}",
                    "driver_number": driver["driver_number"],
                    "position": driver_result["position"],
                    "number_of_laps": driver_result["number_of_laps"],
                    "qualifying_results": qualifying_results,
                    "dnf": driver_result["dnf"],
                    "dns": driver_result["dns"],
                    "dsq": driver_result["dsq"]
                }
            )

    return {
        "team": team_name,
        "session_key": session_key,
        "performance": performance
    }