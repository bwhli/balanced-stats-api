from ..helpers import hex_to_int
from ..icx import Icx


class BalanceToken:

    def __init__(self):
        self._icx = Icx()
        self._icx_price = self._icx.get_icx_usd_price()
        self._BALANCED_DEX_ADDRESS = "cxa0af3165c08318e988cb30993b3048335b94af6c"  # noqa 503
        self._BALANCE_TOKEN_CONTRACT_ADDRESS = "cxf61cd5a45dc9f91c15aa65831a30a90d59a09619"  # noqa 503

    def get_baln_staked_supply(self):
        baln_staked_supply = self._icx.call(self._BALANCE_TOKEN_CONTRACT_ADDRESS, "totalStakedBalance")  # noqa 503
        return hex_to_int(baln_staked_supply, 18)

    def get_baln_total_supply(self):
        baln_total_supply = self._icx.call(self._BALANCE_TOKEN_CONTRACT_ADDRESS, "totalSupply")  # noqa 503
        return hex_to_int(baln_total_supply, 18)

    def get_baln_circulating_supply(self):
        # Circulating supply is Total Supply minus 10% (DAO and emergency fund), minus staked supply.  # noqa 503
        return (self.get_baln_total_supply() * 0.9) - self.get_baln_staked_supply()  # noqa 503

    def get_baln_price(self):
        baln_price_usd = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPriceByName", {"_name": "BALN/bnUSD"}), 18)  # noqa 503
        baln_price_icx = baln_price_usd / self._icx_price
        return {
            "baln_price_usd": baln_price_usd,
            "baln_price_icx": baln_price_icx
        }

    def get_baln_market_cap(self):
        baln_circulating_supply = self.get_baln_circulating_supply()
        baln_price_usd = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPriceByName", {"_name": "BALN/bnUSD"}), 18)  # noqa 503
        return round(baln_circulating_supply * baln_price_usd, 2)
