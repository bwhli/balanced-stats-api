from ..helpers import hex_to_int
from ..icx import Icx


class BalancedDex:

    def __init__(self):
        self._icx = Icx()
        self._icx_price = self._icx.get_icx_usd_price()
        self._BALANCED_DEX_ADDRESS = "cxa0af3165c08318e988cb30993b3048335b94af6c"  # noqa 503

    def get_pool_stats(self):
        sicx_icx_stats = self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolStats", {"_id": 1})  # noqa 503
        sicx_bnusd_stats = self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolStats", {"_id": 2})  # noqa 503
        baln_bnusd_stats = self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolStats", {"_id": 3})  # noqa 503
        for pool in [sicx_icx_stats, sicx_bnusd_stats, baln_bnusd_stats]:
            pool["base"] = hex_to_int(pool["base"], 18)
            pool["quote"] = hex_to_int(pool["quote"], 18)
            pool["price"] = hex_to_int(pool["price"], 18)
            pool["total_supply"] = hex_to_int(pool["total_supply"], 18)
            pool["base_decimals"] = hex_to_int(pool["base_decimals"], 0)
            pool["quote_decimals"] = hex_to_int(pool["quote_decimals"], 0)
            pool["min_quote"] = hex_to_int(pool["min_quote"], 18)
        return {
            "sicx_icx": sicx_icx_stats,
            "sicx_bnusd": sicx_bnusd_stats,
            "baln_bnusd": baln_bnusd_stats
        }

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
