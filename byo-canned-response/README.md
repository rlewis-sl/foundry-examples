# **byo-canned-response**

Demonstrates a minimal container-based hosted agent for Microsoft Foundry.
- Uses azure-ai-agentserver-responses SDK to expose a Responses protocol endpoint
- "Agent" implementation is a simple canned response: "Hi, Bob"

## Run script locally

```bash
cd byo-canned-response
python3 main.py
```

Once the agent is running, it responds to requests sent to http://localhost:8088/responses

See [Notes/Request Body](#request-body) section for the expected format of the request body.

## Run docker container locally

### Build docker image

```bash
cd byo-canned-response
docker build -t byo-canned-response .
```

### Start docker container

```bash
cd byo-canned-response
docker run -p 8088:808/tcp byo-canned-response
```

Once the container is running, the agent responds to requests sent to http://localhost:8088/responses, the same as when the script is run directly.


## Notes

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

(Can't find good HTTP-level documentation. OpenAI has a Python library, but ultimately it's just HTTP. Note that the response body can be much more complex than shown here.)

Example simple request...

```
POST http://localhost:8088/responses
{
    "input": "Hello"
}
```

### Response Body

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
