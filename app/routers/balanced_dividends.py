from ..models.BalancedDividends import BalancedDividends
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/dividends")

balanced_dividends = BalancedDividends()


class Fees(BaseModel):
    baln_fees: str
    bnusd_fees: str
    icx_fees: str
    sicx_fees: str
    total_fees_usd: str


@router.get("/fees/", response_model=Fees)
async def get_fees():
    fees = balanced_dividends.get_fees()
    bnusd_fees = fees["bnusd_fees"]
    baln_fees = fees["baln_fees"]
    icx_fees = fees["icx_fees"]
    sicx_fees = fees["sicx_fees"]
    total_fees_usd = fees["total_fees_usd"]
    return {
        "bnusd_fees": bnusd_fees,
        "baln_fees": baln_fees,
        "icx_fees": icx_fees,
        "sicx_fees": sicx_fees,
        "total_fees_usd": total_fees_usd
    }
