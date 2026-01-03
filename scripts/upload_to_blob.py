from azure.storage.blob import BlobServiceClient

CONNECTION_STRING = "<YOUR_AZURE_CONNECTION_STRING>"
CONTAINER_NAME = "transactions"
BLOB_NAME = "transactions.csv"

blob_service = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service.get_container_client(CONTAINER_NAME)

try:
    container_client.create_container()
except Exception:
    pass

blob_client = container_client.get_blob_client(BLOB_NAME)

with open("data/transactions.csv", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("✅ Uploaded transactions.csv to Azure Blob Storage")
