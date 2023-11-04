"""An Azure Python Pulumi program"""

from pulumi_azure import core, cosmosdb


resource_group = core.ResourceGroup('resource_group',
                                    name='resource-group-exp',
                                    location='Germany West Central')

account = cosmosdb.Account('account',
                           name='account-exp',
                           resource_group_name=resource_group.name,
                           location=resource_group.location,
                           offer_type='Standard',

                           consistency_policy=cosmosdb.AccountConsistencyPolicyArgs(
                               consistency_level='Strong'
                           ),
                           geo_locations=[
                               cosmosdb.AccountGeoLocationArgs(
                                   location='germanywestcentral',
                                   failover_priority=0
                               )
                           ])

db = cosmosdb.SqlDatabase('sql_database',
                          name='database-exp',
                          resource_group_name=resource_group.name,
                          account_name=account.name)

container = cosmosdb.SqlContainer('container',
                                  name='container-exp',
                                  resource_group_name=resource_group.name,
                                  account_name=account.name,
                                  database_name=db.name,
                                  partition_key_path='/Country',
                                  partition_key_version=1)

