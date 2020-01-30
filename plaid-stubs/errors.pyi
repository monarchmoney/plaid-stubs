from typing import Any, Optional, List, Dict, Mapping


class BaseError(Exception):
    message: str = ...
    type: str = ...
    code: str = ...
    display_message: str = ...
    def __init__(self, message: str, type: str, code: str, display_message: str) -> None: ...

class PlaidError(BaseError):
    request_id: str = ...
    causes: List[PlaidCause] = ...
    def __init__(
            self,
            message: str,
            type: str,
            code: str,
            display_message: str,
            request_id: str = ...,
            causes: Optional[List[Dict[str, str]]] = ...,
    ) -> None: ...
    @staticmethod
    def from_response(response: Dict[str, Any]) -> PlaidError: ...

class PlaidCause(BaseError):
    item_id: str = ...
    def __init__(self, message: str, type: str, code: str, display_message: str, item_id: str) -> None: ...

class InvalidRequestError(PlaidError): ...
class InvalidInputError(PlaidError): ...
class RateLimitExceededError(PlaidError): ...
class APIError(PlaidError): ...
class ItemError(PlaidError): ...
class InstitutionError(PlaidError): ...

PLAID_ERROR_TYPE_MAP: Mapping[str, PlaidError]
