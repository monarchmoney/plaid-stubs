from plaid.api.api import API as API
from typing import Any, Optional, Dict

from ..client import ResponseJSON


class Institutions(API):
    def get(self, count: int, offset: int = ..., _options: Optional[Dict[str, Any]] = ...) -> ResponseJSON: ...
    def get_by_id(self, institution_id: str, _options: Optional[Dict[str, Any]] = ...) -> ResponseJSON: ...
    def search(self, query: str, _options: Optional[Dict[str, Any]] = ..., products: Optional[Any] = ...) -> ResponseJSON: ...
