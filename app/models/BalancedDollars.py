from ..helpers import hex_to_int
from ..icx import Icx


class BalancedDollars:

    def __init__(self):
        self._icx = Icx()
        self._BALANCED_DOLLARS_ADDRESS = "cx88fd7df7ddff82f7cc735c871dc519838cb235bb"  # noqa 503

    def get_bnusd_total_supply(self):
        bnusd_total_supply = self._icx.call(
            self._BALANCED_DOLLARS_ADDRESS, "totalSupply")
        return hex_to_int(bnusd_total_supply, 18)
