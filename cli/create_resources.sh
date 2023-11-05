#!/bin/bash

resourceGroupName="resource-group-exp"
accountName="account-exp"
databaseName="database-exp"
containerName="container-exp"
location="germanywestcentral"

az group create \
    --name $resourceGroupName \
    --location $location

az cosmosdb create \
    --name $accountName \
    --resource-group $resourceGroupName \
    --locations regionName=$location failoverPriority=0 \
    --default-consistency-level Strong

az cosmosdb sql database create \
    --name $databaseName \
    --resource-group $resourceGroupName \
    --account-name $accountName

az cosmosdb sql container create \
    --name $containerName \
    --resource-group $resourceGroupName \
    --account-name $accountName \
    --database-name $databaseName \
    --partition-key-path "/Country" \
    --partition-key-version 1
