from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, conint


class Model(BaseModel):
  '''Base model with custom configuration and encoders.'''

  class Config:
    '''Base model configuration.'''

    json_encoders = {
      datetime: lambda value: value.isoformat(
        timespec = 'milliseconds').replace('+00:00', 'Z')
    }


class Account(Model):
  '''Account model.'''

  active_card: bool = Field(..., alias = 'active-card')
  available_limit: conint(ge = 0) = Field(..., alias = 'available-limit')


class Transaction(Model):
  '''Transaction model.'''

  merchant: str
  amount: conint(ge = 0)
  time: datetime


class AccountResponse(Model):
  '''Account response model.'''

  account: Account
  violations: List[str]
