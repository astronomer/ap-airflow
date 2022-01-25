from google.cloud import storage
from datetime import datetime, timedelta, timezone
import click


@click.command()
@click.argument("bucket_name")
@click.option("--age", "-a", default=30, type=click.INT, help="Age in days")
def delete_blobs(bucket_name, age):
    """
    This script helps to delete old blobs from GCS bucket.

    python clean-artifacts.py <bucket_name> --age <age>
    """
    created_before = datetime.now(tz=timezone.utc) - timedelta(days=age)
    client = storage.Client()
    blobs = client.list_blobs(bucket_name)
    for blob in blobs:
        if blob.time_created < created_before and "dev" in blob.name:
            blob.delete()


if __name__ == "__main__":
    delete_blobs()
