def analysis_router(state):

    question = state["question"].lower()

    analysis_words = [
        "analizează",
        "evoluat",
        "compară",
        "de ce",
        "strategie",
        "performanță",
        "ritm",
        "pace",
        "avantaj",
        "dezavantaj",
        "cum a evoluat"
    ]

    if any(word in question for word in analysis_words):
        return "strategy"

    return "report"