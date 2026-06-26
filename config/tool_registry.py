from tools.context_tools import get_session_context
from tools.driver_tools import get_driver_info
from tools.lap_tools import get_lap_times
from tools.pit_stops_tools import get_pit_stops
from tools.race_control_tools import get_race_control
from tools.stints_tools import get_stints
from tools.team_session_result import get_team_session_result
from tools.team_tools import get_team_info
from tools.standings_tools import get_driver_standings
from tools.weather_tools import get_weather

CONTEXT_TOOLS = [
    get_session_context
]

DATA_TOOLS = [
    get_driver_info,
    get_team_info,
    get_driver_standings,
    get_team_session_result,
    get_weather,
    get_lap_times,
    get_pit_stops,
    get_race_control,
    get_stints,
    get_weather
]

ALL_TOOLS = {
    "get_session_context": get_session_context,
    "get_driver_info": get_driver_info,
    "get_team_info": get_team_info,
    "get_driver_standings": get_driver_standings,
    "get_team_session_result": get_team_session_result,
    "get_weather": get_weather,
    "get_lap_times":get_lap_times,
    "get_pit_stops":get_pit_stops,
    "get_race_control":get_race_control,
    "get_stints":get_stints

}