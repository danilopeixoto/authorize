from pydantic.datetime_parse import parse_datetime


def test_is_initialized(account_state):
  '''Test is_initialized method for account state.'''

  assert account_state.is_initialized() == True

def test_has_active_card(account_state):
  '''Test has_active_card method for account state.'''

  assert account_state.has_active_card() == True

def test_has_sufficient_limit(account_state, transaction):
  '''Test has_sufficient_limit method for account state.'''

  assert account_state.has_sufficient_limit(transaction) == True

def test_get_last_transactions(account_state, transactions):
  '''Test get_last_transactions method for account state.'''

  account_state.transactions = transactions

  since = parse_datetime('2019-02-12T10:00:00.000Z')
  last_transactions = account_state.get_last_transactions(since)

  assert list(last_transactions) == transactions[-4:]

def test_has_high_frequency_transaction(account_state, transaction, transactions):
  '''Test has_high_frequency_transaction method for account state.'''

  account_state.transactions = transactions

  assert account_state.has_high_frequency_transaction(transaction) == True

def test_has_doubled_transaction(account_state, transaction, transactions):
  '''Test has_doubled_transaction method for account state.'''

  account_state.transactions = transactions

  assert account_state.has_doubled_transaction(transaction) == True

def test_release_transaction(account_state, transaction):
  '''Test release_transaction method for account state.'''

  account_state.release_transaction(transaction)

  assert account_state.account.available_limit == 10
