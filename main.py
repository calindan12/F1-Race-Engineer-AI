from dotenv import load_dotenv

from agents.data_analyst import (data_agent,execute_tool)

from agents.race_engineer import (race_engineer_agent)

from graph.workflow import graph


# load_dotenv()

# response = data_agent.invoke(
#     {
#         "question": "Who is leading the championship?"
#     }
# )

# print(response.tool_calls)

# if response.tool_calls:

#     result = execute_tool(
#         response.tool_calls[0]
#     )

#     print("result: " , result)

#     report = race_engineer_agent.invoke(
#         {
#             "driver_data": result
#         }
#     )

#     print("report: " , report)

result = graph.invoke(
    {
        "question": "Cine conduce clasamentul"
    }
)

print(result["report"])

