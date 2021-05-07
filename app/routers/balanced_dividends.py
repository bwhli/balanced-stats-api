from ..models.BalancedDividends import BalancedDividends
from fastapi import APIRouter

router = APIRouter(prefix="/dividends")

balanced_dividends = BalancedDividends()


@router.get("/fees/")
async def get_fees():
    return {
        "total_fees_usd": balanced_dividends.get_fees()
    }
