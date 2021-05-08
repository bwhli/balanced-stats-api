from ..models.BalanceToken import BalanceToken
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/baln")

# Initialize BalanceToken class.
balance_token = BalanceToken()

# Set total supply and staked supply.
baln_total_supply = balance_token.get_baln_total_supply()
baln_circulating_supply = balance_token.get_baln_circulating_supply()
baln_staked_supply = balance_token.get_baln_staked_supply()


class MarketCapModel(BaseModel):
    baln_market_cap: str


class PriceModel(BaseModel):
    baln_price_icx: str
    baln_price_usd: str


class StakeModel(BaseModel):
    baln_percent_staked_of_circulating: str
    baln_percent_staked_of_total: str


class SupplyModel(BaseModel):
    baln_circulating_supply: str
    baln_staked_supply: str
    baln_total_supply: str


@router.get("/market-cap/")
async def get_baln_market_cap():
    """
    Returns the market cap of Balance Token in USD.
    """
    baln_market_cap = balance_token.get_baln_market_cap()
    return {"baln_market_cap": baln_market_cap}


@router.get("/price/", response_model=PriceModel)
async def get_balance_token_price():
    """
    Get Balance Token price in USD and ICX
    """
    baln_price = balance_token.get_baln_price()
    baln_price_icx = baln_price["baln_price_icx"]
    baln_price_usd = baln_price["baln_price_usd"]
    return {
        "baln_price_icx": baln_price_icx,
        "baln_price_usd": baln_price_usd
    }


@router.get("/stake/", response_model=StakeModel)
async def get_balance_token_stake():
    baln_percent_staked_of_total = baln_staked_supply / baln_total_supply
    baln_percent_staked_of_circulating = baln_staked_supply / (baln_total_supply * 0.9)  # noqa 503
    return {
        "baln_percent_staked_of_circulating": baln_percent_staked_of_circulating,  # noqa 503
        "baln_percent_staked_of_total": baln_percent_staked_of_total
    }


@router.get("/supply/", response_model=SupplyModel)
async def get_balance_token_supply():
    return {
        "baln_circulating_supply": baln_circulating_supply,
        "baln_staked_supply": baln_staked_supply,
        "baln_total_supply": baln_total_supply,
    }
