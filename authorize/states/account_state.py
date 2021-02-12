from datetime import timedelta
import itertools

from ..models import Account


class AccountState:
  '''Global account state.'''

  def __init__(self, account):
    '''Initialize account state.'''

    self.account = account
    self.transactions = []

  def is_initialized(self):
    '''Return true if the account is initialized, otherwise false.'''

    return self.account is not None

  def has_active_card(self):
    '''Return true if the account has an active card, otherwise false.'''

    return self.account.active_card

  def has_sufficient_limit(self, transaction):
    '''Return true if the account has sufficient limit, otherwise false.'''

    return self.account.available_limit >= transaction.amount

  def get_transactions_by_time_interval(self, start_time, end_time):
    '''Filter transactions by time interval.'''

    return (transaction for transaction in self.transactions
      if start_time <= transaction.time < end_time)

  def has_low_transaction_frequency(
      self, transaction, interval = timedelta(minutes = 2), count = 3):
    '''Return true if the account has low transaction frequency, otherwise false.'''

    initial_time = transaction.time - interval
    end_time = transaction.time

    return len(list(
      self.get_transactions_by_time_interval(initial_time, end_time))) < count

  def has_doubled_transaction(
      self, transaction, interval = timedelta(minutes = 2)):
    '''Return true if the account has doubled transaction, otherwise false.'''

    initial_time = transaction.time - interval
    end_time = transaction.time

    transactions = itertools.chain(
      self.get_transactions_by_time_interval(initial_time, end_time),
      [transaction])

    unique_transactions = set(
      frozenset(transaction.dict(exclude = {'time'}).items())
        for transaction in transactions)

    return len(list(transactions)) != len(unique_transactions)

  def release_transaction(self, transaction):
    '''Release transaction operation.'''

    self.account = Account(
      available_limit = self.account.available_limit - transaction.amount,
      **self.account.dict(exclude = {'available_limit'}))

    self.transactions.append(transaction)
