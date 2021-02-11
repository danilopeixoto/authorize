from .models import Model, Account, Transaction


class AccountOperation(Model):
  '''Account operation model.'''

  account: Account


class TransactionOperation(Model):
  '''Transaction operation model.'''

  transaction: Transaction


__all__ = [
  'AccountOperation',
  'TransactionOperation'
]
