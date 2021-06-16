from plaid.model_utils import ApiTypeError as ApiTypeError, ModelComposed as ModelComposed, ModelNormal as ModelNormal, ModelSimple as ModelSimple, cached_property as cached_property, change_keys_js_to_python as change_keys_js_to_python, convert_js_args_to_python_args as convert_js_args_to_python_args, file_type as file_type, none_type as none_type, validate_get_composed_info as validate_get_composed_info
from typing import Any

class DepositSwitchAltCreateResponse(ModelNormal):
    allowed_values: Any = ...
    validations: Any = ...
    attribute_map: Any = ...
    required_properties: Any = ...
    deposit_switch_id: Any = ...
    request_id: Any = ...
    def __init__(self, deposit_switch_id: Any, request_id: Any, *args: Any, **kwargs: Any) -> None: ...
