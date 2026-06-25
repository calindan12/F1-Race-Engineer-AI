from dotenv import load_dotenv
from langchain_groq import ChatGroq
from config.tool_registry import CONTEXT_TOOLS
from tools.driver_tools import get_driver_info
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.llm import llm


load_dotenv()


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Ești un Agent Contextual F1. Singura ta responsabilitate este să identifici evenimentul de Formula 1 menționat de utilizator. Folosește instrumentele disponibile pentru a recupera meeting_key-ul corect și session_key-ul. Nu răspunde la întrebarea utilizatorului."
    ),
    (
        "human",
        "{question}"
    )
])

llm_tools = llm.bind_tools(CONTEXT_TOOLS)

context_agent = prompt | llm_tools

