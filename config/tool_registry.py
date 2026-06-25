from tools.context_tools import get_session_context
from tools.driver_tools import get_driver_info
from tools.team_session_result import get_team_session_result
from tools.team_tools import get_team_info
from tools.standings_tools import get_driver_standings

CONTEXT_TOOLS = [
    get_session_context
]

DATA_TOOLS = [
    get_driver_info,
    get_team_info,
    get_driver_standings,
    get_team_session_result
]

ALL_TOOLS = {
    "get_session_context": get_session_context,
    "get_driver_info": get_driver_info,
    "get_team_info": get_team_info,
    "get_driver_standings": get_driver_standings,
    "get_team_session_result": get_team_session_result
}