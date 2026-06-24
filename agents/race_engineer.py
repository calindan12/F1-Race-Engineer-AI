from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools.driver_tools import get_driver_info
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.llm import llm



load_dotenv()


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Ești inginer de curse de Formula 1. Creează un raport DOAR din datele furnizate. Nu inventa analize de performanță, recomandări strategice sau fapte care nu sunt prezente în datele de intrare. Dacă lipsesc informații, menționează-le explicit."
    ),
    (
        "human",
        "Driver data: {driver_data}"
    )
])

race_engineer_agent  = prompt | llm | StrOutputParser()
