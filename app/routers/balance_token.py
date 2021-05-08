import requests
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


class BalnHolders(BaseModel):
    baln_holders: str


class BalnMarketCap(BaseModel):
    baln_market_cap: str


class BalnPrice(BaseModel):
    baln_price_icx: str
    baln_price_usd: str


class BalnStake(BaseModel):
    baln_percent_staked_of_circulating: str
    baln_percent_staked_of_total: str


class BalnSupply(BaseModel):
    baln_circulating_supply: str
    baln_staked_supply: str
    baln_total_supply: str


@router.get("/holders/", response_model=BalnHolders)
async def get_baln_holders():
    r = requests.get(
        "https://tracker.icon.foundation/v3/token/summary?contractAddr=cxf61cd5a45dc9f91c15aa65831a30a90d59a09619").json()  # noqa 503
    baln_holders = r["data"]["holders"]
    return {"baln_holders": baln_holders}


@router.get("/market-cap/", response_model=BalnMarketCap)
async def get_baln_market_cap():
    """
    Returns the market cap of Balance Token in USD.
    """
    baln_market_cap = balance_token.get_baln_market_cap()
    return {"baln_market_cap": baln_market_cap}


@router.get("/price/", response_model=BalnPrice)
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


@router.get("/stake/", response_model=BalnStake)
async def get_balance_token_stake():
    baln_percent_staked_of_total = baln_staked_supply / baln_total_supply
    baln_percent_staked_of_circulating = baln_staked_supply / (baln_total_supply * 0.9)  # noqa 503
    return {
        "baln_percent_staked_of_circulating": baln_percent_staked_of_circulating,  # noqa 503
        "baln_percent_staked_of_total": baln_percent_staked_of_total
    }


@router.get("/supply/", response_model=BalnSupply)
async def get_balance_token_supply():
    return {
        "baln_circulating_supply": baln_circulating_supply,
        "baln_staked_supply": baln_staked_supply,
        "baln_total_supply": baln_total_supply,
    }
