from dotenv import load_dotenv
from langgraph.types import Command

from rpg_graph import create_graph

# Load environment variables
load_dotenv()

def main():
    """
    Main entry point of the application.
    """
    print("LangGraph application initialized with AWS Bedrock")
    
    # Create and run the graph
    graph = create_graph()
    
    # Initialize the state
    initial_state = {
        "messages": [],
        "next": "welcome",
        "category": None
    }

    # Thread
    thread = {"configurable": {"thread_id": "1"}}
    initial_input = {"input": ""}
    # Run the graph until the first interruption
    for event in graph.stream(initial_input, thread, stream_mode="updates"):
        print(str(event) + "\n")

    for event in graph.stream(Command(resume="I want to create a scenario"), thread, stream_mode="updates"):
        print(str(event) + "\n")

if __name__ == "__main__":
    main() 