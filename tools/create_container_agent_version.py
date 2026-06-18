import os
import time

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import AgentProtocol, ContainerConfiguration,HostedAgentDefinition, ProtocolVersionRecord
from azure.identity import DefaultAzureCredential, AzureCliCredential
from dotenv import load_dotenv


load_dotenv()

FOUNDRY_PROJECT_ENDPOINT = os.environ.get("FOUNDRY_PROJECT_ENDPOINT", "<missing environment variable>")
ACR_ID = os.environ.get("ACR_ID", "<missing environment variable>")

image_name = "byo-canned-response-hosted:latest"

# credential = DefaultAzureCredential()
credential = AzureCliCredential()
project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=credential,
    allow_preview=True     # hosted agents is still a preview feature
)

agent = project.agents.create_version(
    agent_name="byo-canned-response-hosted-container-agent-test",
    definition=HostedAgentDefinition(
        cpu="0.5",
        memory="1Gi",
        protocol_versions=[ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="1.0.0")],
        container_configuration=ContainerConfiguration(
            image=f"{ACR_ID}.azurecr.io/{image_name}",
        ),
        # environment_variables={},     # TODO: Add support for environment variables?
    ),
    # description="Hosted agent version description"   # TODO: Add support for description
)

print(f"Created agent version: {agent.name} (version = {agent.version}) with image: {image_name}")

# TODO: Move this code to a helper function in another module.
while True:
    version_info = project.agents.get_version(agent_name=agent.name, agent_version=agent.version)
    status = version_info["status"]
    # print(f"Agent provisioning status: {status}.")

    if status == "active":
        print("Agent is ready.")
        break
    elif status == "failed":
        print(f"Agent provisioning failed: {version_info['error']}.")
        break

    time.sleep(3)
