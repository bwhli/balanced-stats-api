from ..helpers import hex_to_int
from ..icx import Icx
from ..models.BalanceToken import BalanceToken


class BalancedDividends:

    def __init__(self):
        self._icx = Icx()
        self.balance_token = BalanceToken()
        self._icx_usd_price = self._icx.get_icx_usd_price()
        self._baln_usd_price = self.balance_token.get_baln_price()["baln_price_usd"]  # noqa 503
        self._BALANCED_DIVIDENDS_ADDRESS = "cx13f08df7106ae462c8358066e6d47bb68d995b6d"  # noqa 503

    def get_fees(self):
        fees = self._icx.call(self._BALANCED_DIVIDENDS_ADDRESS, "getBalances", None)  # noqa 503
        sicx_fees = hex_to_int(fees["sICX"], 18)
        bnusd_fees = hex_to_int(fees["bnUSD"], 18)
        baln_fees = hex_to_int(fees["BALN"], 18)
        icx_fees = hex_to_int(fees["ICX"], 18)
        total_fees_usd = sicx_fees * self._icx_usd_price + baln_fees * \
            self._baln_usd_price + icx_fees * self._icx_usd_price + bnusd_fees
        return {
            "sicx_fees": sicx_fees,
            "bnusd_fees": bnusd_fees,
            "baln_fees": baln_fees,
            "icx_fees": icx_fees,
            "total_fees_usd": total_fees_usd
        }
