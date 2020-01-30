from plaid.api.api import API as API
from plaid.client import Client
from typing import Any, Optional, List, Dict

from ..client import ResponseJSON


class Balance(API):
    def get(self, access_token: str, _options: Optional[List[str]] = ..., account_ids: Optional[List[str]] = ...) -> ResponseJSON: ...

class Accounts(API):
    balance: Balance = ...
    def __init__(self, client: Client) -> None: ...
    def get(self, access_token: str, _options: Optional[Dict[str, Any]] = ..., account_ids: Optional[List[str]] = ...) -> ResponseJSON: ...
