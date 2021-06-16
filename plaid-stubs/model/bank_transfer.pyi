from plaid.model_utils import ApiTypeError as ApiTypeError, ModelComposed as ModelComposed, ModelNormal as ModelNormal, ModelSimple as ModelSimple, cached_property as cached_property, change_keys_js_to_python as change_keys_js_to_python, convert_js_args_to_python_args as convert_js_args_to_python_args, file_type as file_type, none_type as none_type, validate_get_composed_info as validate_get_composed_info
from typing import Any

def lazy_import() -> None: ...

class BankTransfer(ModelNormal):
    allowed_values: Any = ...
    validations: Any = ...
    attribute_map: Any = ...
    required_properties: Any = ...
    id: Any = ...
    ach_class: Any = ...
    account_id: Any = ...
    type: Any = ...
    user: Any = ...
    amount: Any = ...
    iso_currency_code: Any = ...
    description: Any = ...
    created: Any = ...
    status: Any = ...
    network: Any = ...
    cancellable: Any = ...
    metadata: Any = ...
    origination_account_id: Any = ...
    direction: Any = ...
    def __init__(self, id: Any, ach_class: Any, account_id: Any, type: Any, user: Any, amount: Any, iso_currency_code: Any, description: Any, created: Any, status: Any, network: Any, cancellable: Any, metadata: Any, origination_account_id: Any, direction: Any, *args: Any, **kwargs: Any) -> None: ...
