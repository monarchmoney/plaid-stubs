from plaid.api.api import API as API

from ..client import ResponseJSON


class Processor(API):
    def stripeBankAccountTokenCreate(self, access_token: str, account_id: str) -> ResponseJSON: ...
    def dwollaBankAccountTokenCreate(self, access_token: str, account_id: str) -> ResponseJSON: ...
