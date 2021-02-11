class Controller:
  '''Abstract operation controller.'''

  def process(self, operation, account_state):
    raise NotImplementedError('abstract class method.')


class AccountController(Controller):
  '''Account controller.'''

  def __init__(self):
    pass


class TransactionController(Controller):
  '''Transaction controller.'''

  def __init__(self):
    pass


__all__ = [
  'AccountController',
  'TransactionController'
]
