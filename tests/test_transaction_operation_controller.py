from authorize.models import (
  TransactionViolation,
  Account,
  AccountResponse)


def test_transaction_account_violation(
    transaction_operation_controller,
    transaction_operation,
    uninitialized_account_state):
  '''Test transaction account violation.'''

  response = transaction_operation_controller.process(
    transaction_operation, uninitialized_account_state)

  assert response == AccountResponse(
    account = uninitialized_account_state.account,
    violations = [
      TransactionViolation.account_not_initialized,
      TransactionViolation.card_not_active,
      TransactionViolation.insufficient_limit])

def test_transaction_inactive_card_violation(
    transaction_operation_controller,
    transaction_operation,
    inactive_card_account_state):
  '''Test transaction inactive card violation.'''

  response = transaction_operation_controller.process(
    transaction_operation, inactive_card_account_state)

  assert response == AccountResponse(
    account = inactive_card_account_state.account,
    violations = [
      TransactionViolation.card_not_active])

def test_transaction_insufficient_limit_violation(
    transaction_operation_controller,
    transaction_operation,
    insufficient_limit_account_state):
  '''Test transaction insufficient limit violation.'''

  response = transaction_operation_controller.process(
    transaction_operation, insufficient_limit_account_state)

  assert response == AccountResponse(
    account = insufficient_limit_account_state.account,
    violations = [
      TransactionViolation.insufficient_limit])

def test_transaction_frequency_violation(
    transaction_operation_controller,
    high_frequency_transaction_operations,
    account_state):
  '''Test transaction frequency violation.'''

  *_, response = (
    transaction_operation_controller.process(operation, account_state)
    for operation in high_frequency_transaction_operations)

  assert response == AccountResponse(
    account = Account(active_card = True, available_limit = 60),
    violations = [
      TransactionViolation.high_frequency_small_interval])

def test_transaction_doubled_violation(
    transaction_operation_controller,
    doubled_transaction_operations,
    account_state):
  '''Test transaction doubled violation.'''

  *_, response = (
    transaction_operation_controller.process(operation, account_state)
    for operation in doubled_transaction_operations)

  assert response == AccountResponse(
    account = Account(active_card = True, available_limit = 90),
    violations = [
      TransactionViolation.doubled_transaction])

def test_release_transaction(
    transaction_operation_controller,
    transaction_operation,
    account_state):
  '''Test release transaction.'''

  response = transaction_operation_controller.process(
    transaction_operation, account_state)

  assert response == AccountResponse(
    account = Account(active_card = True, available_limit = 10),
    violations = [])
