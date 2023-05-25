from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema, SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    print(f'The input id {id}')
    summary = await crud.get(id)
    if summary:
        return summary
    else:
        raise HTTPException(status_code=404, detail="Record Not Found")


@router.get("/", response_model=list[SummarySchema])
async def get_all_summaries() -> list[SummarySchema]:
    summary_list = await crud.get_list()
    if summary_list:
        return summary_list
    else:
        raise HTTPException(status_code=404, details="Records Not Found")
