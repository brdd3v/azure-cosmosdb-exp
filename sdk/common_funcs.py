import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.cosmosdb import CosmosDBManagementClient

load_dotenv()

CREDENTIAL = DefaultAzureCredential()
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")

RESOURCE_GROUP_NAME = "resource-group-exp"
ACCOUNT_NAME = "account-exp"
DATABASE_NAME = "database-exp"
CONTAINER_NAME = "container-exp"


def get_resource_client():
    return ResourceManagementClient(credential=CREDENTIAL, subscription_id=SUBSCRIPTION_ID)


def get_cosmos_db_mgmt_client():
    return CosmosDBManagementClient(credential=CREDENTIAL, subscription_id=SUBSCRIPTION_ID)
