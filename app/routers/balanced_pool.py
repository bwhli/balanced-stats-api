from ..models.BalancedDex import BalancedDex
from fastapi import APIRouter

router = APIRouter(prefix="/pool")

# Initialize BalancedDex class.
balanced_dex = BalancedDex()


@router.get("/")
async def get_pool_stats():
    return balanced_dex.get_pool_stats()
