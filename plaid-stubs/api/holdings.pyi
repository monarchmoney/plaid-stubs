from plaid.api.api import API as API

from ..client import ResponseJSON


class Holdings(API):
    def get(self, access_token: str) -> ResponseJSON: ...
