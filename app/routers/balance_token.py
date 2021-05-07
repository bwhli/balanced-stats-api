from ..models.BalanceToken import BalanceToken
from fastapi import APIRouter

router = APIRouter(prefix="/baln")

# Initialize BalanceToken class.
balance_token = BalanceToken()

# Set total supply and staked supply.
baln_total_supply = balance_token.get_baln_total_supply()
baln_staked_supply = balance_token.get_baln_staked_supply()


@router.get("/supply/")
async def get_balance_token_supply():
    return {
        "baln_total_supply": baln_total_supply,
        "baln_staked_supply": baln_staked_supply,
    }


@router.get("/stake/")
async def get_balance_token_stake():
    baln_percent_staked_of_total = baln_staked_supply / baln_total_supply
    baln_percent_staked_of_circulating = baln_staked_supply / (baln_total_supply * 0.9)  # noqa 503
    return {
        "baln_percent_staked_of_total": baln_percent_staked_of_total,
        "baln_percent_staked_of_circulating": baln_percent_staked_of_circulating  # noqa 503
    }


@router.get("/price/")
async def get_balance_token_price():
    """
    Get Balance Token price in USD and ICX
    """
    return balance_token.get_baln_price()
