import re
from ..helpers import hex_to_int
from ..icx import Icx


class BalancedDex:

    def __init__(self):
        self._icx = Icx()
        self._icx_price = self._icx.get_icx_usd_price()
        self._BALANCED_DEX_ADDRESS = "cxa0af3165c08318e988cb30993b3048335b94af6c"  # noqa 503

    def get_price(self, market):
        valid_markets = ["sICX/ICX", "sICX/bnUSD", "BALN/bnUSD"]
        if market in valid_markets:
            params = {"_name": market}
            price = self._icx.call(
                self._BALANCED_DEX_ADDRESS, "getPriceByName", params)
            return market, hex_to_int(price)
        else:
            return f"ERROR: {market} is not a supported market."

    def get_pool_stats(self, pool):
        pool_id = self._pool_name_to_id(pool)
        params = {"_id": pool_id}
        base, quote = re.findall(r"(.*)\/(.*)", pool)[0]
        pool_stats = self._icx.call(
            self._BALANCED_DEX_ADDRESS, "getPoolStats", params)
        return pool, hex_to_int(pool_stats['base']), hex_to_int(pool_stats['quote'])  # noqa 503

    def get_dex_tvl(self):
        sicx_icx_tvl = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "totalSupply", {"_id": 1}), 18)  # noqa 503
        sicx_bnusd_tvl = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolTotal", {"_id": 2, "_token": "cx88fd7df7ddff82f7cc735c871dc519838cb235bb"}), 18)  # noqa 503
        baln_bnusd_tvl = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolTotal", {"_id": 3, "_token": "cx88fd7df7ddff82f7cc735c871dc519838cb235bb"}), 18)  # noqa 503
        sicx_icx_tvl_usd = sicx_icx_tvl * self._icx_price
        dex_total_tvl_usd = sicx_bnusd_tvl + baln_bnusd_tvl + sicx_icx_tvl_usd
        return {
            "sicx_icx_tvl": sicx_icx_tvl,
            "sicx_bnusd_tvl": sicx_bnusd_tvl,
            "baln_bnusd_tvl": baln_bnusd_tvl,
            "dex_total_tvl_usd": dex_total_tvl_usd
        }

    def _pool_name_to_id(self, pool):
        if pool == "sICX/ICX":
            return 1
        elif pool == "sICX/bnUSD":
            return 2
        elif pool == "BALN/bnUSD":
            return 3
        else:
            raise Exception
