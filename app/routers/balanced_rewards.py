from ..models.BalancedRewards import BalancedRewards
from fastapi import APIRouter

router = APIRouter(prefix="/rewards")

# Initialize BalanceToken class.
balanced_rewards = BalancedRewards()


@router.get("/apy/")
async def get_apy():
    return balanced_rewards.get_apy()
