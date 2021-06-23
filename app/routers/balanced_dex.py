from ..models.BalancedDex import BalancedDex
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/dex")

# Initialize BalancedDex class.
balanced_dex = BalancedDex()


class MarketQuote(BaseModel):
    sicx_icx_quote: str
    sicx_bnusd_quote: str
    baln_bnusd_quote: str


@router.get("/quote/", response_model=MarketQuote)
async def get_market_quotes():
    market_quotes = balanced_dex.get_market_quotes()
    sicx_icx_quote = market_quotes[0]
    sicx_bnusd_quote = market_quotes[1]
    baln_bnusd_quote = market_quotes[2]
    return {
        "sicx_icx_quote": sicx_icx_quote,
        "sicx_bnusd_quote": sicx_bnusd_quote,
        "baln_bnusd_quote": baln_bnusd_quote
    }
