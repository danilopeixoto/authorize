class Validator:
  '''Validation wrapper.'''

  precedence = 0

  def __init__(self, function):
    '''Initialize validation wrapper.'''

    self.function = function
    self.precedence = Validator.precedence

    Validator.precedence += 1

  def __call__(self, *args, **kwargs):
    '''Call validation function.'''

    return self.function(*args, **kwargs)


def validator(function):
  '''Validation decorator.'''

  return Validator(function)
