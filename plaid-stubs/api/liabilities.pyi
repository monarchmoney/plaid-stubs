from plaid.api.api import API as API
from typing import Any, Optional, List, Dict

from ..client import ResponseJSON


class Liabilities(API):
    def get(self, access_token: str, _options: Optional[Dict[str, Any]] = ..., account_ids: Optional[List[str]] = ...) -> ResponseJSON: ...
