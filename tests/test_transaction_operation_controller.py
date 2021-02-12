from authorize.models import TransactionViolation, AccountResponse

def test_transaction_account_violation(
    transaction_operation_controller, transaction_operation, uninitialized_account_state):
  '''Test transaction account violation.'''

  response = transaction_operation_controller.process(
    transaction_operation, uninitialized_account_state)

  assert response == AccountResponse(
    account = account_state.account,
    violations = [TransactionViolation.account_not_initialized])
