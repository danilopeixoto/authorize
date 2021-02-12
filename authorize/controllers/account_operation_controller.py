from ..models import AccountViolation, AccountResponse
from ..decorators import validator
from .operation_controller import OperationController


class AccountOperationController(OperationController):
  '''Account operation controller.'''

  @validator
  def validate_account_initialization(self, operation, account_state):
    '''Validate account initialization.'''

    return ([]
      if not account_state.is_initialized()
      else [AccountViolation.account_already_initialized])

  def process(self, operation, account_state):
    '''Validate rules and create account.'''

    violations = self.validate(operation, account_state)

    if len(violations) == 0:
      account_state.account = operation.account

    return AccountResponse(
      account = account_state.account,
      violations = violations)
