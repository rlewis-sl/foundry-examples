import asyncio

from azure.ai.agentserver.responses import (
    CreateResponse,
    ResponseContext,
    ResponsesAgentServerHost,
    # ResponsesServerOptions,
    TextResponse,
)

app = ResponsesAgentServerHost(
    configure_observability=None,
)

@app.response_handler
async def handler(
    request: CreateResponse,
    context: ResponseContext,
    cancellation_signal: asyncio.Event
) -> TextResponse:
    return TextResponse(context, request, text="Hi, Bob!")

app.run()
