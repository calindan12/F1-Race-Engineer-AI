from agents.data_analyst import execute_tool
from tools.context_tools import get_session_context
from agents.context_agent import context_agent


def context_node(state):
    print("state primit: " , state)
    response = context_agent.invoke({
        "question":state["question"],
    })

    tool_call = response.tool_calls[0]
    result = execute_tool(tool_call)
    
    return {
        "meeting_key": result["meeting_key"],
        "session_key": result["session_key"],
        "country_name": result["country_name"],
        "session_name": result["session_name"],
        "year": result["year"]
    }
    