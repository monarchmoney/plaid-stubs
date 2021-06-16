from plaid.model_utils import ApiTypeError as ApiTypeError, ModelComposed as ModelComposed, ModelNormal as ModelNormal, ModelSimple as ModelSimple, cached_property as cached_property, change_keys_js_to_python as change_keys_js_to_python, convert_js_args_to_python_args as convert_js_args_to_python_args, file_type as file_type, none_type as none_type, validate_get_composed_info as validate_get_composed_info
from typing import Any

def lazy_import() -> None: ...

class LiabilityOverride(ModelNormal):
    allowed_values: Any = ...
    validations: Any = ...
    attribute_map: Any = ...
    required_properties: Any = ...
    type: Any = ...
    purchase_apr: Any = ...
    cash_apr: Any = ...
    balance_transfer_apr: Any = ...
    special_apr: Any = ...
    last_payment_amount: Any = ...
    minimum_payment_amount: Any = ...
    is_overdue: Any = ...
    origination_date: Any = ...
    principal: Any = ...
    nominal_apr: Any = ...
    interest_capitalization_grace_period_months: Any = ...
    repayment_model: Any = ...
    expected_payoff_date: Any = ...
    guarantor: Any = ...
    is_federal: Any = ...
    loan_name: Any = ...
    loan_status: Any = ...
    payment_reference_number: Any = ...
    pslf_status: Any = ...
    repayment_plan_description: Any = ...
    repayment_plan_type: Any = ...
    sequence_number: Any = ...
    servicer_address: Any = ...
    def __init__(self, type: Any, purchase_apr: Any, cash_apr: Any, balance_transfer_apr: Any, special_apr: Any, last_payment_amount: Any, minimum_payment_amount: Any, is_overdue: Any, origination_date: Any, principal: Any, nominal_apr: Any, interest_capitalization_grace_period_months: Any, repayment_model: Any, expected_payoff_date: Any, guarantor: Any, is_federal: Any, loan_name: Any, loan_status: Any, payment_reference_number: Any, pslf_status: Any, repayment_plan_description: Any, repayment_plan_type: Any, sequence_number: Any, servicer_address: Any, *args: Any, **kwargs: Any) -> None: ...