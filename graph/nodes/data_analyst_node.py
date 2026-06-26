import json
from agents.data_analyst import (data_agent, execute_tool)

def data_analyst_node(state):
    print("state data_analyst_node:", state)

    agent_input = {
        "question": state["question"],
        "session_key": state.get("session_key", "")
    }

    response = data_agent.invoke(agent_input)
    print("Tool calls detectate:", response.tool_calls)

    if not response.tool_calls:
        return {"tool_result": "Nu s-au putut colecta date din unelte."}

    combined_results = []

    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        print(f"Se execută unealta: {tool_name}")
        
        try:
            result = execute_tool(tool_call)
        except Exception as e:
            result = f"Eroare: {str(e)}"

        if tool_name == 'get_weather':
            weather_list = []
            
            if isinstance(result, str):
                try: result = json.loads(result)
                except: pass
            
            if isinstance(result, dict):
                for key in ["weather", "results", "data"]:
                    if key in result and isinstance(result[key], list):
                        weather_list = result[key]
                        break
                if not weather_list:
                    weather_list = [result]
            elif isinstance(result, list):
                weather_list = result

            
            if len(weather_list) > 100:
                pas = 8  
            elif len(weather_list) > 30:
                pas = 3  
            else:
                pas = 1  
                
            sampled_weather = weather_list[::pas]
            print(f"Se aplică filtrarea cu pasul {pas}. Rezultat final: {len(sampled_weather)} linii.")
            
            cleaned_weather = []
            for entry in sampled_weather:
                if isinstance(entry, dict):
                    cleaned_weather.append({
                        "date": entry.get("date"),
                        "track_temp": entry.get("track_temperature"),
                        "air_temp": entry.get("air_temperature"),
                        "rain": entry.get("rainfall")
                    })
            result = cleaned_weather
        elif isinstance(result, list) and len(result) > 20:
            result = result[:15]
            
        combined_results.append({
            "tool": tool_name,
            "data": result
        })

    formatted_tool_result = ""
    for res in combined_results:
        formatted_tool_result += f"\n--- DATE DIN UNEALTA: {res['tool']} ---\n"
        formatted_tool_result += json.dumps(res['data'], indent=2) if isinstance(res['data'], (dict, list)) else str(res['data'])
        formatted_tool_result += "\n"

    print(formatted_tool_result[:300] + "... [DATE TOTALE SALVATE]")

    return {
        "tool_result": formatted_tool_result
    }