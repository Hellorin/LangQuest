from langchain_core.messages import SystemMessage, HumanMessage

from bedrock import get_bedrock_chat_model
from graph.state import AgentState
from utils.prompt_loader import load_prompt


def sorry_handler_node(state: AgentState) -> AgentState:
    """
    Node that handles cases where the user's input couldn't be properly categorized.
    Provides a helpful response and guidance to the user.
    """
    user_message = state["messages"][-1]

    chat_model = get_bedrock_chat_model()

    # Load and format the sorry handler prompt
    context_prompt = load_prompt(
        "context",
        {}
    )

    sorry_prompt = load_prompt(
        "sorry_handler",
        {"user_input": user_message.content}
    )

    # Get the response from the model
    response = chat_model.invoke([
        SystemMessage(content=context_prompt),
        HumanMessage(content=sorry_prompt),
    ])

    # Add the response to the messages
    state["messages"].append(response)

    return {
        "messages": state["messages"],
        "category": None
    } 