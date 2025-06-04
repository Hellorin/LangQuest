from langchain_core.messages import HumanMessage
from langgraph.types import interrupt

from graph.state import AgentState


def user_input_node(state: AgentState) -> AgentState:
    """
    Node that handles user input before categorization.
    """
    feedback = interrupt("What do you want to do?")
    state["messages"].append(HumanMessage(feedback))

    # Add the last message to the state
    return {
        "messages": state["messages"],
        "category": None
    }