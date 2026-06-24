from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools.driver_tools import get_driver_info
from langchain_core.prompts import ChatPromptTemplate
from agents.race_engineer import race_engineer_agent
from tools.standings_tools import get_driver_standings
from tools.team_tools import get_team_info



load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

llm_tools = llm.bind_tools([get_driver_info , get_team_info, get_driver_standings])


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Esti Data Analyst de F1"
    ),
    (
        "human",
        "{question}"
    )
])

agent = prompt | llm_tools

response = agent.invoke({
    "question": "Who is leading the championship?"
})

print(response.tool_calls)


if response.tool_calls:

    call = response.tool_calls[0]

    tool_name = call["name"]

    if tool_name == "get_driver_info":
        result = get_driver_info.invoke(call["args"])

    elif tool_name == "get_team_info":
        result = get_team_info.invoke(call["args"])

    elif tool_name == "get_driver_standings":
        result = get_driver_standings.invoke(call["args"])

    print(result)

    report = race_engineer_agent.invoke(
        {
            "driver_data": result
        }
    )

    print(report)

