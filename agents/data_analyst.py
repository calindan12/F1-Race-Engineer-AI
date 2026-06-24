from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from tools.driver_tools import get_driver_info
from tools.team_tools import get_team_info
from tools.standings_tools import get_driver_standings
from config.llm import llm


llm_tools = llm.bind_tools([
    get_driver_info,
    get_team_info,
    get_driver_standings
])

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Esti Data Analyst de Formula 1."
    ),
    (
        "human",
        "{question}"
    )
])

data_agent = prompt | llm_tools


def execute_tool(tool_call):

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    tools = {
        "get_driver_info": get_driver_info,
        "get_team_info": get_team_info,
        "get_driver_standings": get_driver_standings
    }

    return tools[tool_name].invoke(tool_args)