from agents.data_analyst import (data_agent,execute_tool)


def data_analyst_node(state):
    print("state primit: " , state)
    response = data_agent.invoke({
        "question":state["question"]
    })
    tool_call = response.tool_calls[0]
    result = execute_tool(tool_call)
    return{
        "tool_result":result
    }