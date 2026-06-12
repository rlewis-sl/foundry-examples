# **anthropic-pass-through**

Microsoft Foundry example demonstrating
- calling an Anthropic API endpoint exposed via Microsoft Foundry
- agent constructed using the AnthropicFoundry extension of the Claude Agent SDK

In this configuration, the API endpoint simply passes through to an Anthropic-hosted endpont.  
Foundry only adds authentication and billing.


## Setup

### Create a Foundry model deployment

- From a Foundry project page (e.g. [rlewis-staffing-test](https://ai.azure.com/foundryProject/overview?wsid=/subscriptions/49b12438-21fd-4814-8fb2-84b3f521d137/resourceGroups/rlewis-test/providers/Microsoft.CognitiveServices/accounts/rlewis-staffing-test-resource/projects/rlewis-staffing-test&tid=89796215-91b2-4b6d-b90b-e8fe588f6336)) ...
- Select "Models + endpoints" link in the left menu bar (under "My assets")
- Select "+ Deploy model" > "Deploy base model"
- Choose a model (e.g. claude-sonnet-4-6)
- "Confirm"
- Select Industry (e.g. "Consulting")
- Click "Agree and Proceed"
- Set deployment name (e.g. "staffing-sonnet46")
- Deployment type = "Global Standard" (no other options)
- Deployment details (defaults)
  - Model version = 1
  - Content safety = DefaultV2
  - Authentication type = Key
  - Resource location = Sweden Central
  - Version upgrade policy = Once a new default verson
- Click "Deploy"

A model deployment is linked to a base model (e.g. "gpt-chat-latest" or "claude-opus-4-7"). It can be configured to automatically update to new versions of the base model when they are published. (Not sure of the details on how that works.)
