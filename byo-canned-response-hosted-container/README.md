# **byo-canned-response-hosted-container**

Demonstrates a minimal container-based hosted agent for Microsoft Foundry.
- Uses azure-ai-agentserver-responses SDK to expose a Responses protocol endpoint
- "Agent" implementation is a simple canned response: "Hi, Bob"

See [byo-canned-response/README.md](../byo-canned-response/README.md) for more information about the agent and how to run it locally.

## Build the docker image

```bash
cd byo-canned-response-hosted-container
docker build -t byo-canned-response-hosted .
```

## Push the docker image to Azure Container Registry


## Create a container-based hosted agent in Microsoft Foundry


## Make requests to the hosted agent


