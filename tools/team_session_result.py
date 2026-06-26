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

        if driver_result:
            session_breakdown = []

            durations = driver_result.get("duration")
            gaps = driver_result.get("gap_to_leader")

            if isinstance(durations, list) and isinstance(gaps, list):
                for i in range(len(durations)):
                    session_breakdown.append(
                        {
                            "segment": f"Q{i + 1}",
                            "duration": durations[i],
                            "gap_to_leader": gaps[i]
                        }
                    )
            else:
                session_breakdown.append(
                    {
                        "segment": "Final Result",
                        "duration": durations,
                        "gap_to_leader": gaps
                    }
                )

            performance.append(
                {
                    "driver": f"{driver['first_name']} {driver['last_name']}",
                    "driver_number": driver["driver_number"],
                    "position": driver_result.get("position"),
                    "number_of_laps": driver_result.get("number_of_laps"),
                    "session_breakdown": session_breakdown,
                    "dnf": driver_result.get("dnf"),
                    "dns": driver_result.get("dns"),
                    "dsq": driver_result.get("dsq")
                }
            )

    return {
        "team": team_name,
        "session_key": session_key,
        "performance": performance
    }