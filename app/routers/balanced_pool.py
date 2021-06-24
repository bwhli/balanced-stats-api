from ..models.BalancedDex import BalancedDex
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/pool")

# Initialize BalancedDex class.
balanced_dex = BalancedDex()

# Fetch stats for all liquidity pools.
pool_stats = balanced_dex.get_pool_stats()


class LiquidityPool(BaseModel):
    sicx_icx_pool: dict
    sicx_bnusd_pool: dict
    baln_bnusd_pool: dict
    baln_sicx_pool: dict


@router.get("/", response_model=LiquidityPool)
async def get_pool_stats():
    sicx_icx_pool = pool_stats["sicx_icx_pool"]
    sicx_bnusd_pool = pool_stats["sicx_bnusd_pool"]
    baln_bnusd_pool = pool_stats["baln_bnusd_pool"]
    baln_sicx_pool = pool_stats["baln_sicx_pool"]
    return {
        "sicx_icx_pool": sicx_icx_pool,
        "sicx_bnusd_pool": sicx_bnusd_pool,
        "baln_bnusd_pool": baln_bnusd_pool,
        "baln_sicx_pool": baln_sicx_pool
    }
