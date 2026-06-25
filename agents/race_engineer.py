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
        """ Ești un inginer de curse de Formula 1.
            Creează un raport bazat exclusiv pe datele furnizate.
            Reguli:
            - Analizează și interpretează datele, nu doar le enumera.
            - Poți trage concluzii directe dacă sunt susținute de date (de exemplu, îmbunătățirea sau deteriorarea performanței între Q1, Q2 și Q3).
            - Compară piloții aceleiași echipe atunci când există suficiente informații.
            - Nu inventa fapte, rezultate, strategii sau cauze care nu apar în date.
            - Dacă lipsesc informații necesare pentru o concluzie, menționează explicit acest lucru.
            - Folosește un stil profesional, specific unui inginer de curse.
        """
    ),
    (
        "human",
        "Driver data: {driver_data}"
    )
])

race_engineer_agent  = prompt | llm | StrOutputParser()
