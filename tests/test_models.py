from authorize.models import AccountResponse
from authorize.operations import AccountOperation, TransactionOperation

import utils


def test_account_operation():
  '''Test account operation model.'''

  data = utils.read_json_file('data/account_operation.json')
  assert utils.parse_json_model(AccountOperation(**data)) == data


def test_transaction_operation():
  '''Test transaction operation model.'''

  data = utils.read_json_file('data/transaction_operation.json')
  assert utils.parse_json_model(TransactionOperation(**data)) == data

def test_account_response():
  '''Test account response model.'''

  data = utils.read_json_file('data/account_response.json')
  assert utils.parse_json_model(AccountResponse(**data)) == data
