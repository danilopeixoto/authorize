from typing import List, Union

from pydantic import Field, conint

from .model import Model
from .violations import AccountViolation, TransactionViolation


class Account(Model):
  '''Account model.'''

  active_card: bool = Field(..., alias = 'active-card')
  available_limit: conint(ge = 0) = Field(..., alias = 'available-limit')


class AccountResponse(Model):
  '''Account response model.'''

  account: Account
  violations: List[Union[AccountViolation, TransactionViolation]]
