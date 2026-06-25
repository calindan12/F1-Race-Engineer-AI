from agents.router_agent import router_agent

def router(state):

    decision = router_agent.invoke(
        {
            "question": state["question"]
        }
    )

    print("Router:", decision)

    if "CONTEXT" in decision.upper():
        return "context"

    return "data_analyst"