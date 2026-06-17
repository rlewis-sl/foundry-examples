# **byo-canned-response**

Demonstrates a minimal container-based hosted agent for Microsoft Foundry.
- Uses azure-ai-agentserver-responses SDK to expose a Responses protocol endpoint
- "Agent" implementation is a simple canned response: "Hi, Bob"


Based on this example: https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/bring-your-own/responses/hello-world

BUT EVEN SIMPLER!

Also see: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/agentserver/azure-ai-agentserver-responses/docs/handler-implementation-guide.md

### Route Mapping

The host automatically maps five endpoints:

- `POST /responses` — Create a response
- `GET /responses/{response_id}` — Retrieve a response (JSON or SSE replay)
- `POST /responses/{response_id}/cancel` — Cancel a response
- `DELETE /responses/{response_id}` — Delete a response
- `GET /responses/{response_id}/input_items` — List input items (paginated)

### Request Body

The Responses protocol is essentially the OpenAI /responses API.

Example simple request...

```
POST http://localhost:8088/responses
{
    "input": "Hello"
}
```

Example response body...

```
{
    "id": "caresp_5bb6722829d70235007tEGRHoNnXUpEKaCCASYRqpG0a5cl1Uw",
    "object": "response",
    "output": [
        {
            "type": "message",
            "id": "msg_5bb6722829d7023500SRpWhauPO6QGETmvmQ0vbFZqzPXQVHGa",
            "role": "assistant",
            "content": [
                {
                    "type": "output_text",
                    "text": "Hi, Bob!",
                    "annotations": [],
                    "logprobs": []
                }
            ],
            "status": "completed",
            "response_id": "caresp_5bb6722829d70235007tEGRHoNnXUpEKaCCASYRqpG0a5cl1Uw",
            "agent_reference": null
        }
    ],
    "created_at": 1781671983,
    "status": "completed",
    "completed_at": 1781671983,
    "response_id": "caresp_5bb6722829d70235007tEGRHoNnXUpEKaCCASYRqpG0a5cl1Uw",
    "agent_reference": {
        "type": "agent_reference"
    },
    "model": "",
    "agent_session_id": "2bd66cbf46fae271e4efb9fbf3a9d20dbf3aa1c1089b3ee577be60f2750c035",
    "background": false
}
```


## Deployment

1. Build the Docker image
2. Push Docker image to Azure Container Registry (ACR)
3. Create an agent in Foundry that deploys containers based on the image to serve agent requests
