from langchain_core.messages import SystemMessage, HumanMessage

from bedrock import get_bedrock_chat_model
from graph.state import AgentState
from utils.prompt_loader import load_prompt


def end_node(state: AgentState) -> AgentState:
    """
    Node that handles the end of the conversation.
    """
    chat_model = get_bedrock_chat_model()

    # Load and format the end prompt
    context_prompt = load_prompt(
        "context",
        {}
    )

    end_prompt = load_prompt(
        "end",
        {}
    )

    # Get the response from the model
    response = chat_model.invoke([
        SystemMessage(content=context_prompt),
        HumanMessage(content=end_prompt),
    ])

    # Add the response to the messages
    state["messages"].append(response)

    return {
        "messages": state["messages"],
        "category": None
    } 