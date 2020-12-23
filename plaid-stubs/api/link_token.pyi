from plaid.api.api import API as API
from typing import Any, Dict, List, Optional
from typing_extensions import TypedDict

from ..client import ResponseJSON


class LinkConfig(TypedDict, total=False):
    user: Dict[str, Any]
    client_name: str
    products: List[str]
    country_codes: List[str]
    language: str
    redirect_uri: Optional[str]
    android_package_name: Optional[str]
    webhook: Optional[str]
    link_customization_name: Optional[str]
    access_token: Optional[str]
    account_filters: Optional[Any]
    cross_app_item_add: Optional[Any]
    payment_initiation: Optional[Any]


class LinkToken(API):
    def create(self, config: LinkConfig) -> ResponseJSON: ...
    def get(self, link_token: str) -> ResponseJSON: ...