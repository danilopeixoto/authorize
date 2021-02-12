from datetime import timedelta

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

  def get_last_transactions(self, since):
    '''Filter last transactions.'''

    return (transaction for transaction in self.transactions
      if transaction.time >= since)

  def has_high_frequency_transaction(
      self, transaction, interval = timedelta(minutes = 2), count = 3):
    '''Return true if the account has high frequency transaction, otherwise false.'''

    last_transactions = self.get_last_transactions(transaction.time - interval)

    return len(list(last_transactions)) + 1 > count

  def has_doubled_transaction(
      self, transaction, interval = timedelta(minutes = 2)):
    '''Return true if the account has doubled transaction, otherwise false.'''

    last_transactions = (transaction.dict(exclude = {'time'})
      for transaction in self.get_last_transactions(transaction.time - interval))

    return transaction.dict(exclude = {'time'}) in last_transactions

  def release_transaction(self, transaction):
    '''Release transaction operation.'''

    self.account = Account(
      available_limit = self.account.available_limit - transaction.amount,
      **self.account.dict(exclude = {'available_limit'}))

    self.transactions.append(transaction)
