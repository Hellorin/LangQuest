from typing import Literal

from graph.state import AgentState

def getCategoryNode(state: AgentState) -> str:
    if state["category"] == "<sorry>":
        return "sorry"
    else:
        if state["category"] == "<character>":
            return "character_creation"
        elif state["category"] == "<scenario>":
            return "scenario_creation"

    return "end"
