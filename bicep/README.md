## NOTES


To build the Bicep file to a JSON template:

```
bicep build main.bicep
```

or

```
az bicep build --file main.bicep
```


To deploy to a subscription:

```
az deployment sub create --location germanywestcentral --name cosmos-exp --template-file main.json
```

