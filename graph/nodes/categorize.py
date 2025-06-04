from langchain_core.messages import SystemMessage, HumanMessage

from bedrock import get_bedrock_chat_model
from graph.state import AgentState
from utils.prompt_loader import load_prompt


def categorize_node(state: AgentState) -> AgentState:
    """
    Node that categorizes the user's input into predefined categories.
    """
    user_message = state["messages"][-1]

    chat_model = get_bedrock_chat_model()

    # Load and format the categorization prompt
    context_prompt = load_prompt(
        "context",
        {}
    )

    categorization_prompt = load_prompt(
        "categorization",
        {"user_input": user_message.content}
    )

    # Get the category from the model
    response = chat_model.invoke([
        SystemMessage(content=context_prompt),
        HumanMessage(content=categorization_prompt),
    ])

    category = response.content.strip().lower()

    # Validate the category
    valid_categories = ["<scenario>", "<character>", "<help>", "<sorry>"]
    if category not in valid_categories:
        category = "<sorry>"

    return {
        "messages": state["messages"],
        "category": category
    }