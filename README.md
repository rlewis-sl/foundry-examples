# foundry-examples
Examples of AI Agents to be deployed to Microsoft Foundry

## Microsoft Foundry Resources

- Subscription: [scottlogic-it-dev](https://portal.azure.com/#@scottlogic.com/resource/subscriptions/49b12438-21fd-4814-8fb2-84b3f521d137/overview)
- Resource Group: [rlewis-test](https://portal.azure.com/#@scottlogic.com/resource/subscriptions/49b12438-21fd-4814-8fb2-84b3f521d137/resourceGroups/rlewis-test/overview)
- Foundry project: [rlewis-staffing-test](https://ai.azure.com/foundryProject/overview?wsid=/subscriptions/49b12438-21fd-4814-8fb2-84b3f521d137/resourceGroups/rlewis-test/providers/Microsoft.CognitiveServices/accounts/rlewis-staffing-test-resource/projects/rlewis-staffing-test&tid=89796215-91b2-4b6d-b90b-e8fe588f6336) (with resource `rlewis-staffing-test-resource`)
- Foundry project API Key: see Foundry Project page
- Foundry project endpoint: https://rlewis-staffing-test-resource.services.ai.azure.com/api/projects/rlewis-staffing-test

## Azure Container Registry Resources

- Same subcription as Foundry: [scottlogic-it-dev](https://portal.azure.com/#@scottlogic.com/resource/subscriptions/49b12438-21fd-4814-8fb2-84b3f521d137/overview)
- Container registry: [49b1243rlewisstaffingtest41eeacr](https://portal.azure.com/#@scottlogic.com/resource/subscriptions/49b12438-21fd-4814-8fb2-84b3f521d137/resourceGroups/rlewis-test/providers/Microsoft.ContainerRegistry/registries/49b1243rlewisstaffingtest41eeacr/overview)


## Required Permissions

See:
- [Sample enterprise RBAC mappings for projects | Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry?tabs=owner#sample-enterprise-rbac-mappings-for-projects)
- [Hosted agent permissions reference | Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agent-permissions)

**Foundry Project Manager**: required for deploying hosted agents; scoped to Foundry resource allows creating Foundry projects and assigning the Foundry User role (hosted agents have a service identity which must be explicitly assigned the Foundry User role)

**Container Repository Writer**: Allows for read and write access to Azure Container Registry repositories (scoped to a specific ACR); excludes catalog listing

## Documentation

Online:
- [Deploy a hosted agent | Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent)
- [Azure Container Registry client library for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/containerregistry-readme?view=azure-python)

Local:
- Foundry [ContainerAgent schema](ContainerAgent.yaml) for `agent.yaml`
