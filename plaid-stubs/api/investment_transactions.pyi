from plaid.api.api import API as API
from typing import Any, Optional, Dict, List

from ..client import ResponseJSON


class InvestmentTransactions(API):
    def get(self,
            access_token: str,
            start_date: str,
            end_date: str,
            _options: Optional[Dict[str, Any]] = ...,
            account_ids: Optional[List[str]] = ...,
            count: Optional[int] = ...,
            offset: Optional[int] = ...,
    ) -> ResponseJSON: ...
