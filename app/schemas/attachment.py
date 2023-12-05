from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class AttachmentBase(BaseModel):
    bucket: str
    key: str
    filename: str


class AttachmentUploadResponse(AttachmentBase):
    signed_url: str


