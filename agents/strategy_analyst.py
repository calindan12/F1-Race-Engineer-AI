from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.llm import llm

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
    """
        You are an F1 Strategy Engineer.
        Analyze ONLY the provided data.

        Identify:
        - performance trends
        - tyre strategy
        - pace changes
        - position changes
        - possible reasons for the results

        Do not invent facts.
        If information is missing, explicitly state that it is unavailable.
        Do not call tools.
    """
    ),
    (
        "human",
    """
        Question:
        {question}

        Available data:
        {tool_result}
    """
        )
    ])

strategy_agent = prompt | llm | StrOutputParser()