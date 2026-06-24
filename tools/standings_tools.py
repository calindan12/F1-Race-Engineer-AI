from langchain_core.tools import tool
import requests

@tool
def get_driver_standings()->dict:
    """Returns current driver standings"""
    return {
        "leader": "Oscar Piastri",
        "points": 250
    }