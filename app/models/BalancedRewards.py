from ..icx import Icx
from ..helpers import hex_to_int
from ..models.BalancedDex import BalancedDex
from ..models.BalancedDollars import BalancedDollars


class BalancedRewards:

    def __init__(self):
        self._icx = Icx()
        self._balanced_dex = BalancedDex()
        self._balanced_dollars = BalancedDollars()
        self._BALANCED_REWARDS_CONTRACT_ADDRESS = "cx10d59e8103ab44635190bd4139dbfd682fa2d07e"  # noqa 503

    def get_bnusd_borrow_apy(self):
        platform_day = int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "distStatus")["platform_day"], 16)  # noqa 503
        baln_emission = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getEmission", {"_day": platform_day}), 18)  # noqa 503
        baln_price = self._balanced_dex.get_market_quotes()[2]
        total_bnusd = self._balanced_dollars.get_bnusd_total_supply()
        bnusd_borrow_apy = ((baln_emission * 0.2) * 365 * baln_price) / total_bnusd  # noqa 503
        return bnusd_borrow_apy

    def get_apy(self):
        sicx_icx_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "sICX/ICX"}), 18)  # noqa 503
        sicx_bnusd_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "sICX/bnUSD"}), 18)  # noqa 503
        baln_bnusd_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "BALN/bnUSD"}), 18)  # noqa 503
        #bnusd_borrow_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "Loans"}), 18)  # noqa 503
        bnusd_borrow_apy = self.get_bnusd_borrow_apy()
        return {
            "sicx_icx_apy": round(sicx_icx_apy * 100, 2),
            "sicx_bnusd_apy": round(sicx_bnusd_apy * 100, 2),
            "baln_bnusd_apy": round(baln_bnusd_apy * 100, 2),
            "bnusd_borrow_apy": round(bnusd_borrow_apy * 100, 2),
        }
