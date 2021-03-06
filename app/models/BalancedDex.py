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
        baln_sicx_stats = self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolStats", {"_id": 4})  # noqa 503
        for pool in [sicx_icx_stats, sicx_bnusd_stats, baln_bnusd_stats, baln_sicx_stats]:  # noqa 503
            pool["base"] = str(hex_to_int(pool["base"], 18))
            pool["quote"] = str(hex_to_int(pool["quote"], 18))
            pool["price"] = str(hex_to_int(pool["price"], 18))
            pool["total_supply"] = str(hex_to_int(pool["total_supply"], 18))
            pool["base_decimals"] = str(hex_to_int(pool["base_decimals"], 0))
            pool["quote_decimals"] = str(hex_to_int(pool["quote_decimals"], 0))
            pool["min_quote"] = str(hex_to_int(pool["min_quote"], 18))
        return {
            "sicx_icx_pool": sicx_icx_stats,
            "sicx_bnusd_pool": sicx_bnusd_stats,
            "baln_bnusd_pool": baln_bnusd_stats,
            "baln_sicx_pool": baln_sicx_stats
        }

    def get_dex_tvl(self):
        sicx_icx_tvl = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "totalSupply", {"_id": 1}), 18)  # noqa 503
        sicx_bnusd_tvl = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolTotal", {"_id": 2, "_token": "cx88fd7df7ddff82f7cc735c871dc519838cb235bb"}), 18)  # noqa 503
        baln_bnusd_tvl = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPoolTotal", {"_id": 3, "_token": "cx88fd7df7ddff82f7cc735c871dc519838cb235bb"}), 18)  # noqa 503
        sicx_icx_tvl_usd = sicx_icx_tvl * self._icx_price
        dex_total_tvl_usd = sicx_bnusd_tvl + baln_bnusd_tvl + sicx_icx_tvl_usd  # noqa 503
        return {
            "sicx_icx_tvl": round(sicx_icx_tvl, 8),
            "sicx_bnusd_tvl": round(sicx_bnusd_tvl, 2),
            "baln_bnusd_tvl": round(baln_bnusd_tvl, 2),
            "dex_total_tvl_usd": round(dex_total_tvl_usd, 2)
        }

    def get_market_quotes(self):
        sicx_icx_quote = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPrice", {"_id": 1}), 18)  # noqa 503
        sicx_bnusd_quote = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPrice", {"_id": 2}), 18)  # noqa 503
        baln_bnusd_quote = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPrice", {"_id": 3}), 18)  # noqa 503
        baln_sicx_quote = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "getPrice", {"_id": 4}), 18)  # noqa 503
        return sicx_icx_quote, sicx_bnusd_quote, baln_bnusd_quote, baln_sicx_quote
