#!/usr/bin/env python

from common_funcs import (
    RESOURCE_GROUP_NAME,
    ACCOUNT_NAME,
    DATABASE_NAME,
    CONTAINER_NAME,
    get_cosmos_db_mgmt_client,
    get_resource_client
)


def main():
    resource_client = get_resource_client()
    resource_group = resource_client.resource_groups.create_or_update(
        RESOURCE_GROUP_NAME,
        {
            "location": "Germany West Central"
        }
    )
    print(f"Resource Group: {resource_group.id}")

    cosmos_db_mgmt_client = get_cosmos_db_mgmt_client()
    account = cosmos_db_mgmt_client.database_accounts.begin_create_or_update(
        resource_group_name=RESOURCE_GROUP_NAME,
        account_name=ACCOUNT_NAME,
        create_update_parameters={
            "location": resource_group.location,
            "properties": {
                "createMode": "Default",
                "databaseAccountOfferType": "Standard",
                "locations": [
                    {
                        "failoverPriority": 0,
                        "isZoneRedundant": False,
                        "locationName": "germanywestcentral"
                    }
                ],
                "consistencyPolicy": {
                    "defaultConsistencyLevel": "Strong",
                    "maxIntervalInSeconds": 5,
                    "maxStalenessPrefix": 100
                }
            }
        }
    ).result()
    print(f"Cosmos DB Account: {account.id}")

    database = cosmos_db_mgmt_client.sql_resources.begin_create_update_sql_database(
        resource_group_name=RESOURCE_GROUP_NAME,
        account_name=ACCOUNT_NAME,
        database_name=DATABASE_NAME,
        create_update_sql_database_parameters={
            "location": resource_group.location,
            "properties": {
                "resource": {"id": DATABASE_NAME}
            }
        }
    ).result()
    print(f"Cosmos DB Database: {database.id}")

    container = cosmos_db_mgmt_client.sql_resources.begin_create_update_sql_container(
        resource_group_name=RESOURCE_GROUP_NAME,
        account_name=ACCOUNT_NAME,
        database_name=DATABASE_NAME,
        container_name=CONTAINER_NAME,
        create_update_sql_container_parameters={
            "location": resource_group.location,
            "properties": {
                "resource": {
                    "id": CONTAINER_NAME,
                    "partitionKey": {"kind": "Hash", "paths": ["/Country"], "version": 1},
                }
            }
        }
    ).result()
    print(f"Comos DB Container: {container.id}")


if __name__ == "__main__":
    main()
