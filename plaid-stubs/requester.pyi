from plaid.errors import PlaidError as PlaidError
from typing import Optional, Set, Dict, Callable
from typing_extensions import Literal

from .client import Response


ALLOWED_METHODS: Set[str]
DEFAULT_TIMEOUT: int

METHOD = Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']


def http_request(
        url: str,
        method: Optional[METHOD] = ...,
        data: Optional[dict] = ...,
        headers: Optional[Dict[str, str]] = ...,
        timeout: int = ...,
        is_json: bool = ...,
) -> Response: ...


post_request: Callable[[str, Optional[dict], Optional[Dict[str, str]], int, bool], Response]
