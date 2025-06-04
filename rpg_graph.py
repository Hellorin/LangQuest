from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import Graph, StateGraph

from graph.edges.categorize import getCategoryNode
from graph.nodes.categorize import categorize_node
from graph.nodes.character_creation import character_creation_node
from graph.nodes.end import end_node
from graph.nodes.scenario_creation import scenario_creation_node
from graph.nodes.sorry_handler import sorry_handler_node
from graph.nodes.user_input import user_input_node
from graph.nodes.welcome import welcome_node
from graph.state import AgentState


def create_graph() -> Graph:
    """
    Create the graph with the welcome, user input, and categorization nodes.
    """
    # Create the graph
    workflow = StateGraph(AgentState)

    # Add the nodes
    workflow.add_node("welcome", welcome_node)
    workflow.add_node("user_input", user_input_node)
    workflow.add_node("categorize", categorize_node)
    workflow.add_node("sorry", sorry_handler_node)
    workflow.add_node("character_creation", character_creation_node)
    workflow.add_node("scenario_creation", scenario_creation_node)
    workflow.add_node("end", end_node)

    # Add the edges
    workflow.add_edge("welcome", "user_input")
    workflow.add_edge("user_input", "categorize")
    workflow.add_edge("sorry", "user_input")
    workflow.add_conditional_edges("categorize", getCategoryNode)
    workflow.add_edge("character_creation", "end")
    workflow.add_edge("scenario_creation", "end")

    # Set the entry point
    workflow.set_entry_point("welcome")

    # Compile the graph
    return workflow.compile(checkpointer=MemorySaver())