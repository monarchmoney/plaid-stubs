from plaid.api.api import API as API

from ..client import ResponseJSON


class Identity(API):
    def get(self, access_token: str) -> ResponseJSON: ...
