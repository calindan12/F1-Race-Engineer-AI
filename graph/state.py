from typing import TypedDict

class F1State(TypedDict):
    question:str
    tool_result:dict
    report:str