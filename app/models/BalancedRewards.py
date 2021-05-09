from ..helpers import hex_to_int
from ..icx import Icx


class BalancedRewards:

    def __init__(self):
        self._icx = Icx()
        self._BALANCED_REWARDS_CONTRACT_ADDRESS = "cx10d59e8103ab44635190bd4139dbfd682fa2d07e"  # noqa 503

    def get_apy(self):
        sicx_icx_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "sICX/ICX"}), 18)  # noqa 503
        sicx_bnusd_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "sICX/bnUSD"}), 18)  # noqa 503
        baln_bnusd_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "BALN/bnUSD"}), 18)  # noqa 503
        bnusd_borrow_apy = hex_to_int(self._icx.call(self._BALANCED_REWARDS_CONTRACT_ADDRESS, "getAPY", {"_name": "Loans"}), 18)  # noqa 503
        return {
            "sicx_icx_apy": round(sicx_icx_apy * 100, 2),
            "sicx_bnusd_apy": round(sicx_bnusd_apy * 100, 2),
            "baln_bnusd_apy": round(baln_bnusd_apy * 100, 2),
            "bnusd_borrow_apy": round(bnusd_borrow_apy * 100, 2),
        }
