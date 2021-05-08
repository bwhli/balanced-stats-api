from ..helpers import hex_to_int
from ..icx import Icx


class BalancedLoans:

    def __init__(self):
        self._icx = Icx()
        self._icx_price = self._icx.get_icx_usd_price()
        self._BALANCED_LOANS_ADDRESS = "cx66d4d90f5f113eba575bf793570135f9b10cece1"  # noqa 503

    def get_loans_tvl(self):
        loans_tvl_sicx = hex_to_int(self._icx.call(self._BALANCED_LOANS_ADDRESS, "getTotalCollateral", None), 18)  # noqa 503
        return {
            "loans_tvl_sicx": round(loans_tvl_sicx, 8),
            "loans_tvl_usd": round(loans_tvl_sicx * self._icx_price, 2)
        }
