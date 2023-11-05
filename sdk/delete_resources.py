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
    # cosmos_db_mgmt_client = get_cosmos_db_mgmt_client()

    # cosmos_db_mgmt_client.sql_resources.begin_delete_sql_container(
    #     resource_group_name=RESOURCE_GROUP_NAME,
    #     account_name=ACCOUNT_NAME,
    #     database_name=DATABASE_NAME,
    #     container_name=CONTAINER_NAME,
    # ).result()

    # cosmos_db_mgmt_client.sql_resources.begin_delete_sql_database(
    #     resource_group_name=RESOURCE_GROUP_NAME,
    #     account_name=ACCOUNT_NAME,
    #     database_name=DATABASE_NAME,
    # ).result()

    # cosmos_db_mgmt_client.database_accounts.begin_delete(
    #     resource_group_name=RESOURCE_GROUP_NAME,
    #     account_name=ACCOUNT_NAME,
    # ).result()

    resource_client = get_resource_client()

    print(f"Deleting resource group: {RESOURCE_GROUP_NAME}")
    resource_client.resource_groups.begin_delete(
        resource_group_name=RESOURCE_GROUP_NAME
    ).result()


if __name__ == "__main__":
    main()
