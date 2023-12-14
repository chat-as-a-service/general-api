from typing import Type

from fastapi import HTTPException


class EntityNotFoundException(HTTPException):
    def __init__(self, entity: Type):
        super().__init__(
            status_code=404,
            detail=f"{entity} does not exist",
        )
