import datetime
import uuid
from typing import IO

from google.cloud import storage
from app.core import log
from app.settings import settings

log = log.getLogger(__name__)

storage_client = storage.Client().from_service_account_json(settings.gcp_key_file_path)


def upload_to_gcs(source_file_name: str, source_stream: IO, content_type: str):
    bucket_name = settings.attachment_bucket_name
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = f'attachments/{uuid.uuid4()}'
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_file(source_stream, content_type=content_type)

    log.info(f"File {source_file_name} uploaded to {destination_blob_name}.")
    return bucket_name, destination_blob_name


def generate_signed_url(bucket_name: str, blob_name: str, expiration_hours: int = 8) -> str:
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(hours=expiration_hours),
        method="GET"
    )

    return url
