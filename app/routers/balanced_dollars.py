import requests
from ..models.BalancedDollars import BalancedDollars
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/bnusd")

# Initialize BalanceToken class.
balanced_dollars = BalancedDollars()


class BnusdHolders(BaseModel):
    bnusd_holders: str


class BnusdSupply(BaseModel):
    bnusd_total_supply: str


@router.get("/holders/", response_model=BnusdHolders)
async def get_bnusd_holders():
    r = requests.get(
        "https://tracker.icon.foundation/v3/token/summary?contractAddr=cx88fd7df7ddff82f7cc735c871dc519838cb235bb").json()  # noqa 503
    bnusd_holders = r["data"]["holders"]
    return {"bnusd_holders": bnusd_holders}


@router.get("/supply/", response_model=BnusdSupply)
async def get_balanced_dollars_supply():
    bnusd_total_supply = balanced_dollars.get_bnusd_total_supply()
    return {
        "bnusd_total_supply": bnusd_total_supply
    }
