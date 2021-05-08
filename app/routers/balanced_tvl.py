from ..models.BalancedLoans import BalancedLoans
from ..models.BalancedDex import BalancedDex
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/tvl")

# Initialize BalancedDex and BalancedLoans classes.
balanced_dex = BalancedDex()
balanced_loans = BalancedLoans()

# Set DEX and loans TVL.
dex_tvl = balanced_dex.get_dex_tvl()
loans_tvl = balanced_loans.get_loans_tvl()


class Tvl(BaseModel):
    tvl_usd: str


class LoansTvl(BaseModel):
    loans_tvl_sicx: str
    loans_tvl_usd: str


class DexTvl(BaseModel):
    sicx_icx_tvl: str
    sicx_bnusd_tvl: str
    baln_bnusd_tvl: str
    dex_total_tvl_usd: str


@router.get("/", response_model=Tvl)
async def get_tvl():
    """
    Returns platform TVL in USD.
    """
    tvl_usd = loans_tvl["loans_tvl_usd"] + dex_tvl["dex_total_tvl_usd"]
    return {
        "tvl_usd": tvl_usd
    }


@router.get("/loans/", response_model=LoansTvl)
async def get_loans_tvl():
    """
    Returns Balanced loans TVL in sICX and USD.
    """
    loans_tvl_sicx = loans_tvl["loans_tvl_sicx"]
    loans_tvl_usd = loans_tvl["loans_tvl_usd"]
    return {
        "loans_tvl_sicx": loans_tvl_sicx,
        "loans_tvl_usd": loans_tvl_usd
    }


@router.get("/dex/", response_model=DexTvl)
async def get_dex_tvl():
    """
    Returns TVL of DEX liquidity pools and total DEX TVL.
    """
    baln_bnusd_tvl = dex_tvl["baln_bnusd_tvl"]
    dex_total_tvl_usd = dex_tvl["dex_total_tvl_usd"]
    sicx_bnusd_tvl = dex_tvl["sicx_bnusd_tvl"]
    sicx_icx_tvl = dex_tvl["sicx_icx_tvl"]
    return {
        "baln_bnusd_tvl": baln_bnusd_tvl,
        "dex_total_tvl_usd": dex_total_tvl_usd,
        "sicx_bnusd_tvl": sicx_bnusd_tvl,
        "sicx_icx_tvl": sicx_icx_tvl,
    }
