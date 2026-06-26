
from agents.strategy_analyst import strategy_agent

def strategy_node(state):

    analysis = strategy_agent.invoke(
        {
            "question": state["question"],
            "tool_result": state["tool_result"]
        }
    )

    return {
        "strategy_analysis": analysis
    }