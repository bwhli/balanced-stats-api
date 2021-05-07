from ..models.BalancedDollars import BalancedDollars
from fastapi import APIRouter

router = APIRouter(prefix="/bnusd")

# Initialize BalanceToken class.
balanced_dollars = BalancedDollars()


@router.get("/supply/")
async def get_balanced_dollars_supply():
    return {
        "bnusd_total_supply": balanced_dollars.get_bnusd_total_supply(),
    }
