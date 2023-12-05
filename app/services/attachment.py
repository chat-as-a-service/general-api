from io import BytesIO

from fastapi import UploadFile

from app.repositories import attachment as attachment_repository
from app.schemas.attachment import AttachmentUploadResponse


def upload_attachment(file: UploadFile):
    in_memory_file = BytesIO()
    in_memory_file.write(file.file.read())
    in_memory_file.seek(0)
    bucket_name, blob_name = attachment_repository.upload_to_gcs(
        file.filename, in_memory_file, file.content_type
    )

    return AttachmentUploadResponse(
        bucket=bucket_name,
        key=blob_name,
        filename=file.filename,
        signed_url=attachment_repository.generate_signed_url(bucket_name, blob_name),
    )
