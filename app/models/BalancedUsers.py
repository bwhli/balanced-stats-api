from ..helpers import hex_to_int
from ..icx import Icx


class BalancedUsers:

    def __init__(self):
        self._icx = Icx()
        self._icx_price = self._icx.get_icx_usd_price()
        self._BALANCED_DEX_ADDRESS = "cxa0af3165c08318e988cb30993b3048335b94af6c"  # noqa 503
        self._BALANCED_LOANS_ADDRESS = "cx66d4d90f5f113eba575bf793570135f9b10cece1"  # noqa 503

    def get_liquidity_borrowers(self):
        borrowers = hex_to_int(self._icx.call(self._BALANCED_LOANS_ADDRESS, "getNonzeroPositionCount", None), 0)  # noqa 503
        return borrowers

    def get_liquidity_providers(self):
        sicx_icx_providers = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "totalDexAddresses", {"_id": 1}), 0)  # noqa 503
        sicx_bnusd_providers = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "totalDexAddresses", {"_id": 2}), 0)  # noqa 503
        baln_bnusd_providers = hex_to_int(self._icx.call(self._BALANCED_DEX_ADDRESS, "totalDexAddresses", {"_id": 3}), 0)  # noqa 503
        total_providers = sicx_icx_providers + sicx_bnusd_providers + baln_bnusd_providers  # noqa 503
        return sicx_icx_providers, sicx_bnusd_providers, baln_bnusd_providers, total_providers  # noqa 503
