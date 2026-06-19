import argparse
import os
import time

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import AgentProtocol, AgentVersionDetails, ContainerConfiguration,HostedAgentDefinition, ProtocolVersionRecord
from azure.identity import DefaultAzureCredential, AzureCliCredential
from dotenv import load_dotenv


load_dotenv()

FOUNDRY_PROJECT_ENDPOINT = os.environ.get("FOUNDRY_PROJECT_ENDPOINT", "<missing environment variable>")
ACR_ID = os.environ.get("ACR_ID", "<missing environment variable>")


def create_container_agent_version(project: AIProjectClient, image_name: str, image_tag: str) -> AgentVersionDetails:
    agent = project.agents.create_version(
        agent_name=image_name,
        definition=HostedAgentDefinition(
            cpu="0.5",
            memory="1Gi",
            protocol_versions=[ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="1.0.0")],
            container_configuration=ContainerConfiguration(
                image=f"{ACR_ID}.azurecr.io/{image_name}:{image_tag}",
            ),
            # environment_variables={},     # TODO: Add support for environment variables?
        ),
        # description="Hosted agent version description"   # TODO: Add support for description
    )

    print(f"Created agent version: {agent.name} (version = {agent.version}) with image: {image_name}:{image_tag}")

    return agent


def wait_for_agent_provisioning(project: AIProjectClient, agent_name: str, agent_version: str):
    """
    Waits for the agent provisioning to complete and prints the status.
    """
    print(f"Waiting for agent {agent_name} version {agent_version} to be provisioned...")
    while True:
        version_info = project.agents.get_version(agent_name=agent_name, agent_version=agent_version)
        status = version_info["status"]
        # print(f"Agent provisioning status: {status}.")

        if status == "active":
            print("Agent is ready.")
            break
        elif status == "failed":
            print(f"Agent provisioning failed: {version_info['error']}.")
            break

        time.sleep(3)


def main():
    parser = argparse.ArgumentParser(description="Create a container agent version in Azure AI Project.")
    parser.add_argument("image_name", type=str, help="The name of the container image to use for the agent version.")
    args = parser.parse_args()
    image_name = args.image_name

    # credential = DefaultAzureCredential()
    credential = AzureCliCredential()

    project = AIProjectClient(
        endpoint=FOUNDRY_PROJECT_ENDPOINT,
        credential=credential,
        allow_preview=True     # hosted agents is still a preview feature
    )

    agent = create_container_agent_version(project, image_name, "latest")
    wait_for_agent_provisioning(project, agent.name, agent.version)


if __name__ == "__main__":
    main()