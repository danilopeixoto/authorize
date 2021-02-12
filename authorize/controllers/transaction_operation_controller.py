from ..models import TransactionViolation, AccountResponse
from ..decorators import validator
from .operation_controller import OperationController


class TransactionOperationController(OperationController):
  '''Transaction operation controller.'''

  @validator
  def validate_account_initialization(self, operation, account_state):
    '''Validate account initialization.'''

    return ([]
      if account_state.is_initialized()
      else [TransactionViolation.account_not_initialized])

  @validator
  def validate_account_active_card(self, operation, account_state):
    '''Validate account active card.'''

    return ([]
      if account_state.is_initialized() and account_state.has_active_card()
      else [TransactionViolation.card_not_active])

  @validator
  def validate_account_available_limit(self, operation, account_state):
    '''Validate account available limit.'''

    return ([]
      if account_state.is_initialized()
        and account_state.has_sufficient_limit(operation.transaction)
      else [TransactionViolation.insufficient_limit])

  @validator
  def validate_account_transaction_frequency(self, operation, account_state):
    '''Validate account transaction frequency.'''

    return ([]
      if account_state.has_low_transaction_frequency(operation.transaction)
      else [TransactionViolation.high_frequency_small_interval])

  @validator
  def validate_account_doubled_transaction(self, operation, account_state):
    '''Validate account doubled transaction.'''

    return ([]
      if account_state.has_doubled_transaction(operation.transaction)
      else [TransactionViolation.doubled_transaction])

  def process(self, operation, account_state):
    '''Validate rules and commit transaction.'''

    violations = self.validate(operation, account_state)

    if len(violations) == 0:
      account_state.commit_transaction(operation.transaction)

    return AccountResponse(
      account = account_state.account,
      violations = violations)
