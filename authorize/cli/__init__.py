import sys
from typing import Optional

import typer

from .. import __version__
from ..models import UninitializedAccount
from ..parsers import OperationParser
from ..states import AccountState


app = typer.Typer(add_completion = False)


def show_version(value: bool):
  '''Show version and exit.'''

  if value:
    typer.echo(f'Version: {__version__}')
    raise typer.Exit()

@app.command(context_settings = dict(help_option_names = ['-h', '--help']))
def main(
    version: Optional[bool] = typer.Option(
      None,
      '--version', '-v',
      callback = show_version,
      help = show_version.__doc__)):
  '''Authorize bank transactions.'''

  parser = OperationParser(sys.stdin)
  account_state = AccountState(UninitializedAccount())

  try:
    for operation, controller in parser:
      response = controller.process(operation, account_state)
      typer.echo(response.json(by_alias = True))

    typer.Exit()
  except Exception as exception:
    typer.echo(f'Error: {exception}', err = True)
    typer.Exit(code = -1)


if __name__ == '__main__':
  app()
