import json


def read_text_file(filename):
  '''Read text file format to string.'''

  with open(filename, 'r') as file:
    return file.read()

def read_json_file(filename):
  '''Read JSON file format to dictionary.'''

  with open(filename, 'r') as file:
    return json.load(file)

def parse_json_model(model):
  '''Parse JSON from model to dictionary.'''

  return json.loads(model.json(by_alias = True))
