from pydantic import BaseModel


class AttachmentBase(BaseModel):
    bucket: str
    key: str
    filename: str


class AttachmentUploadResponse(AttachmentBase):
    signed_url: str
