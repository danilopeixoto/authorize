from authorize.models import AccountViolation, AccountResponse


def test_account_initialization(
    account_operation_controller,
    account_operation,
    uninitialized_account_state):
  '''Test account initialization.'''

  response = account_operation_controller.process(
    account_operation, uninitialized_account_state)

  assert response == AccountResponse(
    account = account_operation.account,
    violations = [])

def test_account_update_violation(
    account_operation_controller, account_operation, account_state):
  '''Test account update violation.'''

  response = account_operation_controller.process(
    account_operation, account_state)

  assert response == AccountResponse(
    account = account_state.account,
    violations = [AccountViolation.account_already_initialized])
