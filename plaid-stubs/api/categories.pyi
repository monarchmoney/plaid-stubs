from plaid.api.api import API as API

from ..client import ResponseJSON


class Categories(API):
    def get(self) -> ResponseJSON: ...
