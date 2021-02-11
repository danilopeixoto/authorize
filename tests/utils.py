import json


def read_json_file(filename):
  '''Read JSON file format to dictionary.'''

  data = {}

  with open(filename, 'r') as file:
    data = json.load(file)

  return data

def parse_json_model(model):
  '''Parse JSON from model to dictionary.'''

  return json.loads(model.json(by_alias = True))
