from iconsdk.builder.call_builder import CallBuilder
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider


class Icx:

    def __init__(self):
        self._icon_service = IconService(
            HTTPProvider("https://ctz.solidwallet.io", 3))
        self._nid = 1

    def debug(self):
        return "DEBUG"

    def call(self, to, method, params=None):
        call = CallBuilder()\
            .to(to)\
            .method(method)\
            .params(params)\
            .build()
        return self._icon_service.call(call)

    def get_icx_usd_price(self):
        call = CallBuilder()\
            .to("cx087b4164a87fdfb7b714f3bafe9dfb050fd6b132")\
            .method("get_ref_data")\
            .params({"_symbol": "ICX"})\
            .build()
        result = self._icon_service.call(call)["rate"]
        return int(result, 16) / 1000000000
