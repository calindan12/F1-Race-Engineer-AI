from typing import TypedDict, Optional


class F1State(TypedDict, total=False):
    question: str

    meeting_key: int
    session_key: int
    country_name: str
    session_name: str
    year: int

    tool_result: dict

    strategy_analysis: str

    report: str