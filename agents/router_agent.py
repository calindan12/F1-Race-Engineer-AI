from langchain_core.prompts import ChatPromptTemplate
from config.llm import llm
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([(
    "system",
    """
        You are an F1 Router.
        Your job is to routing the request to either CONTEXT or DATA based on these strict rules:

        - Return "CONTEXT" if the user's question mentions or implies a specific race weekend, year, track, or session (e.g., "Belgia 2023", "Marele Premiu din Monaco", "cursa de duminică trecută"). We must find the official session_key first before querying any timeline or pit stop data.
        
        - Return "DATA" ONLY if the question is general, global, or does not require a specific race ID look up (e.g., "Who is leading the championship?", "Ce echipe concurează anul acesta?").

        Return ONLY one word, exactly as shown below:
        CONTEXT
        or
        DATA
    """
    ),
    (
        "human",
        "{question}"
    )
])

router_agent = prompt | llm | StrOutputParser()