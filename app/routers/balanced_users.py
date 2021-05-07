from ..models.BalancedUsers import BalancedUsers
from fastapi import APIRouter

router = APIRouter(prefix="/users")

# Initialize BalancedLoans class.
balanced_users = BalancedUsers()


@router.get("/borrowers/")
async def get_borrowers():
    """
    Returns the number of borrowers.
    """
    return {
        "borrowers": balanced_users.get_liquidity_borrowers()
    }


@router.get("/providers/")
async def get_liquidity_providers():
    """
    Returns the number of liquidity providers.
    """
    return balanced_users.get_liquidity_providers()
