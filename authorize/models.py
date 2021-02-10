
from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, conint


class Account(BaseModel):
  active_card: bool = Field(..., alias = 'active-card')
  available_limit: conint(ge = 0) = Field(..., alias = 'available-limit')


class Transaction(BaseModel):
  merchant: str
  amount: conint(ge = 0)
  time: datetime


class AccountCreateOperation(BaseModel):
  account: Account


class AccountTransactionOperation(BaseModel):
  transaction: Transaction


class AccountResponse(BaseModel):
  account: Account
  violations: List[str]
