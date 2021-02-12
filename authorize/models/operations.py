from .model import Model
from .account import Account
from .transaction import Transaction


class AccountOperation(Model):
  '''Account operation model.'''

  account: Account


class TransactionOperation(Model):
  '''Transaction operation model.'''

  transaction: Transaction
