from pathlib import Path

from typer.testing import CliRunner
from authorize.cli import app

import utils


runner = CliRunner()


def test_show_version():
  '''Test show_version command.'''

  result = runner.invoke(app, ['--version'])

  assert result.exit_code == 0
  assert 'Version:' in result.stdout

def test_authorization():
  '''Test authorize command.'''

  sample_path = Path('data/')

  samples = [
    'operations',
    'account_operations',
    'transaction_operations',
    'transaction_operations_violations'
  ]

  input_filenames = (sample_path / sample for sample in samples)
  output_filenames = (sample_path / f'{sample}_output' for sample in samples)

  for input_filename, output_filename in zip(input_filenames, output_filenames):
    input = utils.read_text_file(input_filename)
    output = utils.read_text_file(output_filename)

    result = runner.invoke(app, input = input)

    assert result.exit_code == 0
    assert output == result.stdout
