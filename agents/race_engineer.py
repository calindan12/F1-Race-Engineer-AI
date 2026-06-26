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
        """
        Ești un Analist de Date F1 expert. Sarcina ta este să identifici și să apelezi uneltele necesare pentru a răspunde la întrebarea utilizatorului.

        REGULĂ CRITICĂ DE CORELARE A DATELOR:
        - În Formula 1, performanța pneurilor (stints) și strategiile sunt influențate direct de starea asfaltului.
        - **Dacă utilizatorul întreabă despre pneuri, strategii, degradare sau eficiența curselor, ești OBLIGAT să apelezi în paralel AMBELE unelte: atât unealta specifică solicitată (ex: `get_stints`), cât și unealta `get_weather`.**
        - Nu lăsa inginerul de curse fără datele de temperatură ale pistei când analizează pneurile.

        Apelează uneltele cu argumentele corecte extrase din context (session_key, driver_number etc.).
        """
    ),
    (
        "human",
        "Driver data: {driver_data}"
    )
])

race_engineer_agent = prompt | llm | StrOutputParser()