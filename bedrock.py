import os

from langchain_aws import ChatBedrock


def get_bedrock_chat_model():
    """Initialize and return a Bedrock chat model."""
    return ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        region_name=os.getenv("AWS_REGION", "eu-central-1"),
        model_kwargs={
            "temperature": 0.7,
            "top_p": 0.9
        }
    )