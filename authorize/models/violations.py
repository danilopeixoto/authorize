from enum import Enum


class AccountViolation(str, Enum):
  '''Account violations.'''

  account_already_initialized = 'account-already-initialized'


class TransactionViolation(str, Enum):
  '''Transaction violations.'''

  account_not_initialized = 'account-not-initialized'
  card_not_active = 'card-not-active'
  insufficient_limit = 'insufficient-limit'
  high_frequency_small_interval = 'high-frequency-small-interval'
  doubled_transaction = '​doubled-transaction'
