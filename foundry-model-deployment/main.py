# foundry-model-deployment (example agent)

import asyncio
import os

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential, DefaultAzureCredential
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


async def main():
    client = FoundryChatClient(
        # project_endpoint=endpoint,         # will use FOUNDRY_PROJECT_ENDPOINT environment variable if not set here
        # model=deployment,                  # will use FOUNDRY_MODEL environment variable if not set here
        credential=DefaultAzureCredential(), # attempts various methods of determining Azure credentials (e.g. credentials used for Azure CLI via `az login`)
        # credential=AzureCliCredential(),  # uses credentials from Azure CLI (requires `az login`)
    )
    agent = Agent(
        client=client,
        instructions="You are a Scottish football enthusiast and can answer most questions about football with an interesting fact from Scottish football history.",
    )

    try:
        return await agent.run("What is the best goal scored at Hampden Park?")
    except Exception as e:
        # Try an explicit Azure CLI credential manager
        client = FoundryChatClient(
            # project_endpoint=endpoint,         # will use FOUNDRY_PROJECT_ENDPOINT environment variable if not set here
            # model=deployment,                  # will use FOUNDRY_MODEL environment variable if not set here
            # credential=DefaultAzureCredential(), # attempts various methods of determining Azure credentials (e.g. credentials used for Azure CLI via `az login`)
            credential=AzureCliCredential(),  # uses credentials from Azure CLI (requires `az login`)
        )
        agent = Agent(
            client=client,
            instructions="You are a Scottish football enthusiast and can answer most questions about football with an interesting fact from Scottish football history.",
        )
        return await agent.run("What is the best goal scored at Hampden Park?")


if __name__ == "__main__":
    response = asyncio.run(main())
    print(response)
