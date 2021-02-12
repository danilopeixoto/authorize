from .. import utils, models, controllers


class OperationParser:
  '''Operation parser.'''

  def __init__(self, stream):
    '''Initialize parser stream.'''
    self.stream = stream

  def __iter__(self):
    '''Parse operation from stream.'''

    for line in self.stream:
      try:
        data = utils.parse_json_string(line)
        name = next(iter(data)).capitalize()

        operation = getattr(models, f'{name}Operation')
        controller = getattr(controllers, f'{name}OperationController')
      except:
        raise ValueError('invalid operation.')

      yield operation(**data), controller()
