from ..models.BalancedLoans import BalancedLoans
from ..models.BalancedDex import BalancedDex
from fastapi import APIRouter

router = APIRouter(prefix="/tvl")

# Initialize BalancedLoans class.
balanced_dex = BalancedDex()
balanced_loans = BalancedLoans()

# Set DEX and loans TVL.
dex_tvl = balanced_dex.get_dex_tvl()
loans_tvl = balanced_loans.get_loans_tvl()


@router.get("/")
async def get_tvl():
    """
    Returns platform TVL in USD.
    """
    return {
        "tvl": loans_tvl["loans_tvl_usd"] + dex_tvl["dex_total_tvl_usd"]
    }


@router.get("/loans/")
async def get_loans_tvl():
    """
    Returns Balanced loans TVL in sICX and USD.
    """
    return {
        "loans_tvl_sicx": loans_tvl["loans_tvl_sicx"],
        "loans_tvl_usd": loans_tvl["loans_tvl_usd"]
    }


@router.get("/dex/")
async def get_dex_tvl():
    """
    Returns TVL of DEX liquidity pools and total DEX TVL.
    """
    return {
        "sicx_icx_tvl": dex_tvl["sicx_icx_tvl"],
        "sicx_bnusd_tvl": dex_tvl["sicx_bnusd_tvl"],
        "baln_bnusd_tvl": dex_tvl["baln_bnusd_tvl"],
        "dex_total_tvl_usd": dex_tvl["dex_total_tvl_usd"]
    }
