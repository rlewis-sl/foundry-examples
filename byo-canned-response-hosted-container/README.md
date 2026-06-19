# **byo-canned-response-hosted-container**

Demonstrates a minimal container-based hosted agent for Microsoft Foundry.
- Uses azure-ai-agentserver-responses SDK to expose a Responses protocol endpoint
- "Agent" implementation is a simple canned response: "Hi, Bob"

See [byo-canned-response/README.md](../byo-canned-response/README.md) for more information about the agent and how to run it locally.

## Build the docker image

```bash
cd byo-canned-response-hosted-container
docker build -t byo-canned-response .
```

## Push the docker image to Azure Container Registry

[need to add instructions for setting up docker authentication to ACR, using `docker login`]

[should be using unique tags instead of ':latest' for reproducible agent deployments]

```bash
cd byo-canned-response-hosted-container
docker tag byo-canned-response:latest 49b1243rlewisstaffingtest41eeacr.azurecr.io/byo-canned-response:latest
docker push 49b1243rlewisstaffingtest41eeacr.azurecr.io/byo-canned-response:latest
```


## Create a container-based hosted agent in Microsoft Foundry

```bash
cd tools
python3 create_container_agent_version.py byo-canned-response
```


## Make requests to the hosted agent


