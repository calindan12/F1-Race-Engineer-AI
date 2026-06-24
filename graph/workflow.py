from langgraph.graph import (StateGraph,START,END)

from graph.state import F1State

from graph.nodes.data_analyst_node import (data_analyst_node)

from graph.nodes.race_engineer_node import (race_engineer_node)

builder = StateGraph(F1State)

builder.add_node(
    "data_analyst",
    data_analyst_node
)

builder.add_node(
    "race_engineer",
    race_engineer_node
)

builder.add_edge(
    START,
    "data_analyst"
)

builder.add_edge(
    "data_analyst",
    "race_engineer"
)

builder.add_edge(
    "race_engineer",
    END
)

graph = builder.compile()