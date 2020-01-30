from plaid.api.api import API as API
from typing import Any, Optional, Dict, List

from ..client import ResponseJSON


class Auth(API):
    def get(self, access_token: str, _options: Optional[Dict[str, Any]] = ..., account_ids: Optional[List[str]] = ...) -> ResponseJSON: ...
