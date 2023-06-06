from typing import Any
from pydantic import BaseModel


class RequestValidationError(BaseModel):
    loc: list[str]
    msg: str
    type: str


class ConflictError(BaseModel):
    loc: list[str]
    type: str
    msg: str
    info: dict[str, Any]


class UnauthorizedError(BaseModel):
    loc: list[str]
    type: str
    msg: str


class NotFoundError(BaseModel):
    loc: list[str]
    type: str
    msg: str
    info: dict[str, Any]


class HTTPErrorDetails(BaseModel):
    detail: list[
        RequestValidationError | ConflictError | UnauthorizedError | NotFoundError
    ]
