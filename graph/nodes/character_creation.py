from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from bedrock import get_bedrock_chat_model
from graph.state import AgentState
from utils.prompt_loader import load_prompt


def character_creation_node(state: AgentState) -> AgentState:
    """
    Node that handles character creation for the user.
    """
    chat_model = get_bedrock_chat_model()

    # Load and format the character creation prompt
    context_prompt = load_prompt(
        "context",
        {}
    )

    character_creation_context_prompt = load_prompt(
        "character_creation_context",
        {}
    )

    character_creation_prompt = load_prompt(
        "character_creation",
        {}
    )

    # Get the response from the model
    response = chat_model.invoke([
        SystemMessage(content=context_prompt + "\n" + character_creation_context_prompt),
        HumanMessage(content=character_creation_prompt)
    ])

    # Add the response to the messages
    state["messages"].append(response)

    return {
        "messages": state["messages"],
        "category": None
    } 