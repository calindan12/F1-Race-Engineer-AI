from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools.driver_tools import get_driver_info
from langchain_core.prompts import ChatPromptTemplate
from agents.race_engineer import race_engineer_agent



load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

llm_tools = llm.bind_tools([get_driver_info])


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Esti Data Analyst de F1"
    ),
    (
        "human",
        "Ia informatii despre {driver_name}"
    )
])

agent = prompt | llm_tools

response = agent.invoke({"driver_name":"Max Verstappen"})


if response.tool_calls:

    call = response.tool_calls[0]
    print(call["args"])

    result = get_driver_info.invoke(
        call["args"]
    )

    report = race_engineer_agent.invoke(
        {
            "driver_data": result
        }
    )

    print(report)

