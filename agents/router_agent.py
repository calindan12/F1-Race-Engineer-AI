from langchain_core.prompts import ChatPromptTemplate
from config.llm import llm
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([(
    "system",
    """
        You are an F1 Router.
        Decide whether the user's question requires finding a Formula 1 session.
        
        Return ONLY one word:
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