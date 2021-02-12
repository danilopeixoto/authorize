from datetime import datetime

from pydantic import conint

from .model import Model


class Transaction(Model):
  '''Transaction model.'''

  merchant: str
  amount: conint(ge = 0)
  time: datetime
