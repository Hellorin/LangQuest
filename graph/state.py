from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage


class AgentState(TypedDict):
    """State for the agent."""
    messages: list[HumanMessage | SystemMessage]
    category: str | None