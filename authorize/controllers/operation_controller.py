import inspect
from functools import reduce

from ..decorators import Validator


class OperationController:
  '''Abstract operation controller.'''

  def validate(self, operation, account_state):
    '''Apply operation validators.'''

    validators = sorted(
      (function[1] for function in inspect.getmembers(type(self),
        lambda member: isinstance(member, Validator))),
      key = lambda validator: validator.precedence)

    return reduce(
      lambda violations, validator: (
        violations + validator(self, operation, account_state)),
      validators, [])

  def process(self, operation, account_state):
    '''Process operation logic.'''

    raise NotImplementedError('calling abstract method.')
