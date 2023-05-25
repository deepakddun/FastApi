from pydantic import BaseModel
from typing import Union


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummarySchema(SummaryResponseSchema):
    pass
