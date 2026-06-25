# 🏎️ F1 Race Engineer AI

An AI multi-agent system built with **LangGraph** and **LangChain** that analyzes Formula 1 data using the OpenF1 API.

The application routes user requests through specialized AI agents capable of retrieving race data, performing contextual reasoning, and generating race engineering reports.

---

# Architecture

```text
                    User
                      │
                      ▼
                Router Agent
              ┌───────────────┐
              │               │
              ▼               ▼
        Context Agent    Data Agent
              │               ▲
              └───────────────┘
                      │
          Analysis Router (planned)
              │               │
              ▼               ▼
      Strategy Agent     Race Engineer
              │               ▲
              └───────────────┘
                      │
                      ▼
                 Final Report
```

---

# Agents

## Router Agent

Determines which workflow should be executed.

- Requests requiring race/session context → Context Agent
- General driver/team questions → Data Agent

---

## Context Agent

Extracts Formula 1 event information from natural language.

Responsibilities:

- country
- year
- session type
- meeting_key
- session_key

Example:

```
User:
How did Ferrari perform in Belgium 2023?

↓

meeting_key = 1216
session_key = 9141
```

---

## Data Agent

Retrieves factual information using OpenF1 tools.

Current tools:

- get_session_context
- get_driver_info
- get_team_info
- get_driver_standings
- get_team_session_result
- get_weather
- get_lap_times
- get_position_history
- get_stints

---

## Strategy Agent (In Progress)

Analyzes retrieved data.

Responsibilities:

- tyre strategy
- pace evolution
- position changes
- weather impact
- performance trends

Uses only data returned by the Data Agent.

---

## Race Engineer

Produces the final engineering report.

Responsibilities:

- summarize findings
- explain performance
- clearly mention missing information
- never invent facts

---

# Technologies

- Python
- LangChain
- LangGraph
- LangSmith
- Groq LLM
- OpenF1 API

---

# Current Workflow

```
User Question
      │
      ▼
 Router Agent
      │
      ▼
Context Agent (optional)
      │
      ▼
 Data Agent
      │
      ▼
 Strategy Agent (when needed)
      │
      ▼
 Race Engineer
      │
      ▼
 Final Report
```

---

# Example Questions

### Driver

```
Tell me about Max Verstappen.
```

---

### Team

```
How did Ferrari perform during Sprint Qualifying in Belgium 2023?
```

---

### Strategy

```
Analyze Ferrari's tyre strategy during the Belgian Grand Prix 2023.
```

---

### Weather

```
How did track temperature affect Ferrari's performance in Belgium 2023?
```

---

# Project Structure

```
F1/
│
├── agents/
│   ├── context_agent.py
│   ├── data_analyst.py
│   ├── strategy_agent.py
│   └── race_engineer.py
│
├── graph/
│   ├── workflow.py
│   ├── router.py
│   ├── state.py
│   └── nodes/
│
├── tools/
│   ├── context_tools.py
│   ├── driver_tools.py
│   ├── standings_tools.py
│   ├── team_tools.py
│   ├── weather_tools.py
│   ├── lap_tools.py
│   ├── position_tools.py
│   └── stint_tools.py
│
├── config/
│
├── main.py
│
└── README.md
```

---

# Roadmap

- [x] LangGraph workflow
- [x] Router Agent
- [x] Context Agent
- [x] Data Agent
- [x] Race Engineer
- [x] LangSmith tracing
- [x] Weather tool
- [x] Lap Times tool
- [x] Position History tool
- [x] Tyre Stints tool
- [ ] Multi-tool execution
- [ ] Strategy Agent
- [ ] Analysis Router
- [ ] MCP integration
- [ ] Unit tests
- [ ] Docker support

---

# Future Improvements

- Multi-tool planning
- Model Context Protocol (MCP)
- Team Radio analysis
- Race Control analysis
- Pit Stop strategy
- Streaming responses
- Tool retry policies
- Memory support
