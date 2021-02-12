import pytest

from authorize.models import (
  Account,
  Transaction,
  AccountOperation,
  TransactionOperation)

from authorize.controllers import (
  AccountOperationController,
  TransactionOperationController)

from authorize.states import AccountState


@pytest.fixture
def uninitialized_account_state():
  '''Uninitialized account state builder.'''

  return AccountState(None)

@pytest.fixture
def account_state():
  '''Account state builder.'''

  account = Account(active_card = True, available_limit = 100)

  return AccountState(account)

@pytest.fixture
def transaction():
  '''Transation instance builder.'''

  return Transaction(
    merchant = 'Burger King',
    amount = 90,
    time = '2019-02-13T10:00:00.000Z')

@pytest.fixture
def transactions():
  '''Transation collection builder.'''

  transactions = []

  transactions.append(
    Transaction(
      merchant = 'Burger King',
      amount = 20,
      time = '2019-02-10T10:00:00.000Z'))

  transactions.append(
    Transaction(
      merchant = 'Burger King',
      amount = 90,
      time = '2019-02-13T10:00:00.000Z'))

  transactions.append(
    Transaction(
      merchant = 'Netflix',
      amount = 30,
      time = '2019-02-13T10:00:01.000Z'))

  transactions.append(
    Transaction(
      merchant = 'Uber',
      amount = 60,
      time = '2019-02-13T10:00:02.000Z'))

  transactions.append(
    Transaction(
      merchant = 'Netflix',
      amount = 10,
      time = '2019-02-13T10:00:03.000Z'))

  return transactions

@pytest.fixture
def account_operation():
  '''Account operation builder.'''

  account = Account(active_card = True, available_limit = 70)

  return AccountOperation(account = account)

@pytest.fixture
def transaction_operation():
  '''Transaction operation builder.'''

  transaction = Transaction(
    merchant = 'Burger King',
    amount = 90,
    time = '2019-02-13T10:00:00.000Z')

  return TransactionOperation(transaction = transaction)

@pytest.fixture
def account_operation_controller():
  '''Account operation controller builder.'''

  return AccountOperationController()

@pytest.fixture
def transaction_operation_controller():
  '''Transaction operation controller builder.'''

  return TransactionOperationController()
