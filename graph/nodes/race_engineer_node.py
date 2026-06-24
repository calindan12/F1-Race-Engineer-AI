from agents.race_engineer import (race_engineer_agent)


def race_engineer_node(state):

    report = race_engineer_agent.invoke({
            "driver_data": state["tool_result"]
        })
    
    return {
        "report": report
    }