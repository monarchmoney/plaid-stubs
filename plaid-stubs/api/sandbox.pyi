from plaid import Client
from plaid.api.api import API as API
from typing import Any, Optional, List, Dict

from ..client import ResponseJSON


class Item(API):
    def reset_login(self, access_token: str) -> ResponseJSON: ...
    def fire_webhook(self, access_token: str, webhook_code: str) -> ResponseJSON: ...

class PublicToken(API):
    def create(
            self,
            institution_id: str,
            initial_products: List[str],
            _options: Optional[Dict[str, Any]] = ...,
            webhook: Optional[str] = ...,
            transactions__start_date: Optional[str] = ...,
            transactions__end_date: Optional[str] = ...,
    ) -> ResponseJSON: ...

class Sandbox(API):
    item: Item = ...
    public_token: PublicToken = ...
    def __init__(self, client: Client) -> None: ...
