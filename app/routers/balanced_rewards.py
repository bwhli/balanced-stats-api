from ..models.BalancedRewards import BalancedRewards
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/rewards")

# Initialize BalanceToken class.
balanced_rewards = BalancedRewards()

# Fetch APY for all pools.
apy = balanced_rewards.get_apy()


class Apy(BaseModel):
    sicx_icx_apy: str
    sicx_bnusd_apy: str
    baln_bnusd_apy: str
    bnusd_borrow_apy: str


@router.get("/apy/", response_model=Apy)
async def get_apy():
    baln_bnusd_apy = apy["baln_bnusd_apy"]
    sicx_bnusd_apy = apy["sicx_bnusd_apy"]
    sicx_icx_apy = apy["sicx_icx_apy"]
    bnusd_borrow_apy = apy["bnusd_borrow_apy"]
    return {
        "baln_bnusd_apy": baln_bnusd_apy,
        "sicx_bnusd_apy": sicx_bnusd_apy,
        "sicx_icx_apy": sicx_icx_apy,
        "bnusd_borrow_apy": bnusd_borrow_apy
    }
