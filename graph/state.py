from typing import TypedDict

class F1State(TypedDict):
    question:str
    
    meeting_key:int
    session_key:int
    country_name:str
    session_name:str
    year:int

    tool_result:dict
    report:str