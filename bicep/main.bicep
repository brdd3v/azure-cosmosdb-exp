// main.bicep

targetScope = 'subscription'

param location string = 'germanywestcentral'

resource resource_group 'Microsoft.Resources/resourceGroups@2023-07-01' = {
  name: 'resource-group-exp'
  location: location
}

module cosmosdb 'cosmosdb.bicep' = {
  scope: resource_group
  name: 'cosmosdb'
  params: {
    accountName: 'account-exp'
    containerName: 'container-exp'
    databaseName: 'database-exp'
    location: location
  }
}
