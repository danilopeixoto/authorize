from . import utils, operations, controllers


class Parser:
  '''Operation parser.'''

  def __init__(stream):
    '''Initialize parser stream.'''
    self.stream = stream

  def __iter__(self):
    '''Parse operation from stream.'''

    for line in self.stream:
      try:
        data = utils.parse_json_string(line)
        name = data.keys()[0].capitalize()

        operation = getattr(operations, f'{name}Operation')
        controller = getattr(controllers, f'{name}Controller')
      except:
        raise ValueError('invalid operation.')

      yield operation(**data), controller
