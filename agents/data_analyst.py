from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from config.tool_registry import ALL_TOOLS, DATA_TOOLS
from tools.context_tools import get_session_context
from tools.driver_tools import get_driver_info
from tools.team_tools import get_team_info
from tools.standings_tools import get_driver_standings
from config.llm import llm


prompt = ChatPromptTemplate.from_messages([
    (
    "system",
    """
        Ești analist de date Formula 1.Folosește instrumentele disponibile.
        Dacă în întrebare există un Session key, folosește-l atunci când apelezi instrumentele care îl necesită.
    """
    ),
    (
        "human",
        "{question}"
    )
])

llm_tools = llm.bind_tools(DATA_TOOLS)


data_agent = prompt | llm_tools


def execute_tool(tool_call):
    tool = ALL_TOOLS[tool_call["name"]]
    return tool.invoke(tool_call["args"])
