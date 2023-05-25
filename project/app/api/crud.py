from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union, List


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    await summary.save()
    return summary.id


async def get(in_id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=in_id).first().values()
    print(summary)
    if summary:
        return summary
    return None


async def get_list() -> List[Union[dict,None]]:
    summary_list = await TextSummary.all().values()
    print(summary_list)
    if summary_list:
        return summary_list
    return None

