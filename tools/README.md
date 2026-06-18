# **tools** for foundry-examples project

This [documentation page](https://learn.microsoft.com/en-us/python/api/overview/azure/containerregistry-readme?view=azure-python) says you need to specify the `--pre` option in `pip install --pre ...` when installing the Python client library for ACR. **Will try with and without.**

(`pip install azure-containerregistry` succeeds without the `--pre` flag. **Need to check if it does what is required.**)

(Not sure now I will use the Python client library for ACR. Can probably do what is required with `docker`.)


# Hosted Agent (Container)

## Login to ACR

see [Authenticate with Azure Container Registry | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli)

Assumes that the Admin user is enabled for the Container registry ("not recommended for multiple users"). You can enable the admin user for your registry in the Azure portal. In the service menu, under Settings, select Access keys. Then tick the Admin user box to enable the account. The admin username is displayed, along with the two passwords, which you can show or regenerate as needed.

NEED A SECURE METHOD TO MANAGE CREDENTIALS!

For now... record the admin username here and allow the user to copy the password from the Container registry page in Azure portal, or from another secure location, and enter it interactively.

(Unexpected, but when I execute the command below (without any explicit credentials), I get a successful login. I presume some interaction with the VS Code foundry extension and/or the Azure CLI has stored these credentials in a local secure store.)

```bash
docker login 49b1243rlewisstaffingtest41eeacr.azurecr.io
```

## Build Container Image

Build the container image according to the instructions in the specific example.  
Note the container image name.


## Push Container Image to ACR

First create an alias of the image.  
```bash
docker tag <image-name> 49b1243rlewisstaffingtest41eeacr.azurecr.io/<image-name>
```

Then push to ACR.
```bash
docker push 49b1243rlewisstaffingtest41eeacr.azurecr.io/<image-name>
```

## Create Container-based Agent

(Planning on adding command line arguments to this script.)

```bash
cd tools
python create_container_agent_version.py
```

When the script reports "Agent is ready" it has been deployed.

## Test the agent

**Foundry Playground**
- Go to Foundry ("nextgen") project page: https://ai.azure.com/nextgen/r/SbEkOCH9SBSPsoSz9SHRNw,rlewis-test,,rlewis-staffing-test-resource,rlewis-staffing-test/home
- Select "Build" from menu in upper right
- Click on agent name to open agent view
- Chat with the agent in the Playground UI

**Web Page**
- Continuing from the agent view...
- Select "Preview web app" from the "Publish" dropdown in the upper right
- Agent web UI opens in a new browser tab

## Publish to Microsoft 365 Copilot (Just you)

- Continuing from the agent view...
- Select "Teams and Microsoft 365 Copilot" from the "Publish" dropdown in the upper right
- Fill in details on the dialog that appears (Agent name, Publish version, Short description, Description, Developer)
- Click "Next: Publish options" button to continue
- Under "Direct publish", select "Just you" option and click the "Publish" button
- Dialog appears with title "Publish successful" and text "Your agent is now available in the Microsoft 365 Copilot agent store (All agents > Your agents) and in Teams (Apps > Manage your apps)."
- Click the "Done" button on the dialog.

## Enable/Use agent from Microsoft 365 Copilot agent store

- Go to https://m365.cloud.microsoft/chat
- Select "Agents" from the left side menu
- Select the deployed agent under "Your agents"
- Chat UI displayed (with agent name and "Created by <Developer>")

## Publish to Microsoft 365 Copilot (Just you)
