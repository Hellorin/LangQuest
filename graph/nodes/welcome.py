from langchain_core.messages import HumanMessage, SystemMessage

from bedrock import get_bedrock_chat_model
from graph.state import AgentState
from utils.prompt_loader import load_prompt

def welcome_node(_: AgentState) -> AgentState:
    """
    Welcome node that greets the user and sets up the initial state.
    """
    welcome_prompt = load_prompt(
        "context",
        {}
    )

    welcome_message = SystemMessage(
        content = welcome_prompt
    )

    present_yourself_message = HumanMessage(
        content = "Present yourself to the user !"
    )

    chat_model = get_bedrock_chat_model()

    response = chat_model.invoke([welcome_message, present_yourself_message])

    return {
        "messages": [response],
        "category": None
    }
