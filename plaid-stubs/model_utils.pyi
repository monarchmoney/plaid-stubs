import io
from plaid.exceptions import ApiAttributeError as ApiAttributeError, ApiKeyError as ApiKeyError, ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

none_type: Any
file_type = io.IOBase

class cached_property:
    result_key: str = ...
    def __init__(self, fn: Any) -> None: ...
    def __get__(self, instance: Any, cls: Optional[Any] = ...) -> Any: ...

PRIMITIVE_TYPES: Any


class OpenApiModel:
    def set_attribute(self, name: Any, value: Any) -> None: ...
    def __ne__(self, other: Any) -> Any: ...
    def __setattr__(self, attr: Any, value: Any) -> None: ...
    def __getattr__(self, attr: Any) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Any: ...

class ModelSimple(OpenApiModel):
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def get(self, name: Any, default: Optional[Any] = ...) -> Any: ...
    def __getitem__(self, name: Any) -> Any: ...
    def __contains__(self, name: Any) -> Any: ...
    def to_str(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...

class ModelNormal(OpenApiModel):
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def get(self, name: Any, default: Optional[Any] = ...) -> Any: ...
    def __getitem__(self, name: Any) -> Any: ...
    def __contains__(self, name: Any) -> Any: ...
    def to_dict(self) -> Any: ...
    def to_str(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...

class ModelComposed(OpenApiModel):
    def __setitem__(self, name: Any, value: Any) -> None: ...
    __unset_attribute_value__: Any = ...
    def get(self, name: Any, default: Optional[Any] = ...) -> Any: ...
    def __getitem__(self, name: Any) -> Any: ...
    def __contains__(self, name: Any) -> Any: ...
    def to_dict(self) -> Any: ...
    def to_str(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...

COERCION_INDEX_BY_TYPE: Any
UPCONVERSION_TYPE_PAIRS: Any
COERCIBLE_TYPE_PAIRS: Any

def get_simple_class(input_value: Any) -> Any: ...
def check_allowed_values(allowed_values: Any, input_variable_path: Any, input_values: Any) -> None: ...
def is_json_validation_enabled(schema_keyword: Any, configuration: Optional[Any] = ...) -> Any: ...
def check_validations(validations: Any, input_variable_path: Any, input_values: Any, configuration: Optional[Any] = ...) -> None: ...
def order_response_types(required_types: Any) -> Any: ...
def remove_uncoercible(required_types_classes: Any, current_item: Any, spec_property_naming: Any, must_convert: bool = ...) -> Any: ...
def get_required_type_classes(required_types_mixed: Any, spec_property_naming: Any) -> Any: ...
def change_keys_js_to_python(input_dict: Any, model_class: Any) -> Any: ...
def get_type_error(var_value: Any, path_to_item: Any, valid_classes: Any, key_type: bool = ...) -> Any: ...
def deserialize_primitive(data: Any, klass: Any, path_to_item: Any) -> Any: ...
def get_discriminator_class(model_class: Any, discr_name: Any, discr_value: Any, cls_visited: Any) -> Any: ...
def deserialize_model(model_data: Any, model_class: Any, path_to_item: Any, check_type: Any, configuration: Any, spec_property_naming: Any) -> Any: ...
def deserialize_file(response_data: Any, configuration: Any, content_disposition: Optional[Any] = ...) -> Any: ...
def attempt_convert_item(input_value: Any, valid_classes: Any, path_to_item: Any, configuration: Any, spec_property_naming: Any, key_type: bool = ..., must_convert: bool = ..., check_type: bool = ...) -> Any: ...
def is_type_nullable(input_type: Any) -> Any: ...
def is_valid_type(input_class_simple: Any, valid_classes: Any) -> Any: ...
def validate_and_convert_types(input_value: Any, required_types_mixed: Any, path_to_item: Any, spec_property_naming: Any, _check_type: Any, configuration: Optional[Any] = ...) -> Any: ...
def model_to_dict(model_instance: Any, serialize: bool = ...) -> Any: ...
def type_error_message(var_value: Optional[Any] = ..., var_name: Optional[Any] = ..., valid_classes: Optional[Any] = ..., key_type: Optional[Any] = ...) -> Any: ...
def get_valid_classes_phrase(input_classes: Any) -> Any: ...
def convert_js_args_to_python_args(fn: Any) -> Any: ...
def get_additional_properties_model_instances(composed_instances: Any, self: Any) -> Any: ...
def validate_get_composed_info(constant_args: Any, model_args: Any, self: Any) -> Any: ...
