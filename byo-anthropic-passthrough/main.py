import asyncio

from anthropic import AnthropicFoundry
from anthropic.types import TextBlock
from azure.ai.agentserver.responses import (
    CreateResponse,
    ResponseContext,
    ResponsesAgentServerHost,
    # ResponsesServerOptions,
    TextResponse,
)
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

responses_app = ResponsesAgentServerHost(
    configure_observability=None,
)

anthropic_client = AnthropicFoundry(
    # SDK will get these values automatically if defined in ANTHROPIC_FOUNDRY_API_KEY and ANTHROPIC_FOUNDRY_RESOURCE?
    # api_key=os.environ.get("ANTHROPIC_FOUNDRY_API_KEY"),
    # resource=os.environ.get("ANTHROPIC_FOUNDRY_RESOURCE")

    # base_url is mutually exclusive with resource, so only set if not using resource
    # base_url="https://rlewis-staffing-test-resource.services.ai.azure.com/anthropic/"
)


def get_reply_from_anthropic_response(anthropic_response) -> str:
    """
    Extracts the reply text from the Anthropic response object.
    """
    print(f"anthropic_response: {anthropic_response}")

    if hasattr(anthropic_response, "content"):
        content = anthropic_response.content
        print(content)

        if isinstance(content, str):
            return content
        elif isinstance(content, list) and len(content) > 0:
            # If content is a list, concatenate the text from all "text" blocks
            output = ""
            first = True
            for block in content:
                if isinstance(block, TextBlock):
                    print("text block!")
                    print(f"block_text: {block.text}")
                    if first:
                        first = False
                    else:
                        output += "\n\n"  # Add 2 newlines between text blocks
                    output += block.text

            return output

        else:
            raise ValueError("Anthropic response content is empty or not a string/list.")
    else:
        raise ValueError("No 'content' in Anthropic response.")
    

@responses_app.response_handler
async def handler(
    request: CreateResponse,
    context: ResponseContext,

    cancellation_signal: asyncio.Event
) -> TextResponse:
    user_input = await context.get_input_text()

    anthropic_response = anthropic_client.messages.create(
        model="staffing-sonnet46", # Use the DEPLOYMENT name in Microsoft Foundry, if different from the model name.
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_input}],
    )

    reply = get_reply_from_anthropic_response(anthropic_response)

    return TextResponse(context, request, text=reply)

responses_app.run()

