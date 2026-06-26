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
        You are an F1 Data Analyst.

        Your responsibility is to retrieve the data required to answer the user's question.

        Use the available tools to collect factual information.
        You may call one or more tools if needed.

        Rules:
        - Never invent data.
        - Always prefer tool calls over guessing.
        - Use session_key whenever a tool requires it.
        - If the question is about a driver, use the driver-related tools.
        - If the question is about a team, use the team-related tools.
        - If the question is about a specific Formula 1 session, use the session-related tools.
        - If multiple pieces of information are required, call multiple tools.
        - Do not explain the results. Only retrieve the necessary data.
    """
    ),
    (
        "human",
    """
        Question:{question}
        Session key: {session_key}
    """
    )
    ])

llm_tools = llm.bind_tools(DATA_TOOLS)


data_agent = prompt | llm_tools


def execute_tool(tool_call):
    tool = ALL_TOOLS[tool_call["name"]]
    return tool.invoke(tool_call["args"])
