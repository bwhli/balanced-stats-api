from ..models.BalancedDollars import BalancedDollars
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/bnusd")

# Initialize BalanceToken class.
balanced_dollars = BalancedDollars()


class BnusdSupply(BaseModel):
    bnusd_total_supply: str


@router.get("/supply/", response_model=BnusdSupply)
async def get_balanced_dollars_supply():
    bnusd_total_supply = balanced_dollars.get_bnusd_total_supply()
    return {
        "bnusd_total_supply": bnusd_total_supply
    }
