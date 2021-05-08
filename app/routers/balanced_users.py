from ..models.BalancedUsers import BalancedUsers
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users")

# Initialize BalancedLoans class.
balanced_users = BalancedUsers()


class Borrowers(BaseModel):
    borrowers: str


class Providers(BaseModel):
    sicx_icx_providers: str
    sicx_bnusd_providers: str
    baln_bnusd_providers: str
    total_providers: str


@router.get("/borrowers/", response_model=Borrowers)
async def get_borrowers():
    """
    Returns the number of borrowers.
    """
    borrowers = balanced_users.get_liquidity_borrowers()
    return {
        "borrowers": borrowers
    }


@router.get("/providers/", response_model=Providers)
async def get_liquidity_providers():
    """
    Returns the number of liquidity providers.
    """
    sicx_icx_providers, sicx_bnusd_providers, baln_bnusd_providers, total_providers = balanced_users.get_liquidity_providers()  # noqa 503
    return {
        "sicx_icx_providers": sicx_icx_providers,
        "sicx_bnusd_providers": sicx_bnusd_providers,
        "baln_bnusd_providers": baln_bnusd_providers,
        "total_providers": total_providers
    }
