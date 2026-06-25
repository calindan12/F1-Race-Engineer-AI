from agents.data_analyst import (data_agent,execute_tool)

def data_analyst_node(state):

    question = state["question"]

    if state.get("session_key") is not None:
        question += f"\n\nSession key: {state['session_key']}"

    response = data_agent.invoke(
        {
            "question": question
        }
    )
    print("state data_analyst_node: " , state)
    agent_input = {
        "question": state["question"]
    }

    if state.get("session_key") is not None:
        agent_input["session_key"] = state["session_key"]

    response = data_agent.invoke(agent_input)

    print(response.tool_calls)
    tool_call = response.tool_calls[0]
    result = execute_tool(tool_call)
    return{
        "tool_result":result
    }