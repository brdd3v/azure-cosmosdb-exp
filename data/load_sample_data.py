import os
import shutil
import git
import json
from dotenv import load_dotenv
from azure.cosmos import CosmosClient


load_dotenv()

PATH = os.getcwd()
PRIMARY_KEY = os.getenv("PRIMARY_KEY")

SAMPLE_DATA_FILENAME = "VolcanoData.json"
ACCOUNT_NAME = "account-exp"
DATABASE_NAME = "database-exp"
CONTAINER_NAME = "container-exp"


def download_sample_data():
    git.Repo.clone_from(
            url="https://github.com/Azure-Samples/azure-cosmos-db-sample-data.git",
            to_path="/tmp/azure-cosmos-db-sample-data"
    )
    shutil.copy(
        src=f"/tmp/azure-cosmos-db-sample-data/SampleData/{SAMPLE_DATA_FILENAME}",
        dst=f"{PATH}/{SAMPLE_DATA_FILENAME}"
    )
    shutil.rmtree("/tmp/azure-cosmos-db-sample-data", ignore_errors=True)


def load_data(json_data):
    url = f"https://{ACCOUNT_NAME}.documents.azure.com:443/"
    client = CosmosClient(url=url, credential=PRIMARY_KEY)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)
    for sample_data in json_data:
        container.upsert_item(sample_data)


def main():
    if SAMPLE_DATA_FILENAME not in os.listdir(PATH):
        download_sample_data()

    with open(f"{PATH}/{SAMPLE_DATA_FILENAME}", "r") as json_file:
        json_data = json.loads(json_file.read())

    load_data(json_data)


if __name__ == "__main__":
    main()
