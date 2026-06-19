# anthropic-passthrough (example agent)

from anthropic import AnthropicFoundry
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = AnthropicFoundry(
    # SDK will get these values automatically if defined in ANTHROPIC_FOUNDRY_API_KEY and ANTHROPIC_FOUNDRY_RESOURCE?
    # api_key=os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"),
    # resource=os.environ.get("ANTHROPIC_FOUNDRY_RESOURCE")

    # base_url is mutually exclusive with resource, so only set if not using resource
    # base_url="https://rlewis-staffing-test-resource.services.ai.azure.com/anthropic/"
)

message = client.messages.create(
    model="staffing-sonnet46", # Use the DEPLOYMENT name in Microsoft Foundry, if different from the model name.
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain what happened at the European Cup final in 1967."}],
)

# Print out response blocks
print(message.content)
