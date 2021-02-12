import sys
from typing import Optional

import typer

from .. import __version__
from ..parsers import OperationParser
from ..states import AccountState


app = typer.Typer(add_completion = False)


def version(value: bool):
  '''Show version and exit.'''

  if value:
    typer.echo(f'Version: {__version__}')
    raise typer.Exit()

@app.command(context_settings = dict(help_option_names = ['-h', '--help']))
def main(
    version: Optional[bool] = typer.Option(
      None, '--version', '-v', callback = version, help = version.__doc__)):
  '''Authorize bank transactions.'''

  parser = OperationParser(sys.stdin)
  account_state = AccountState(None)

  for operation, controller in parser:
    typer.echo(controller.process(operation, account_state).json())

  typer.Exit()


if __name__ == '__main__':
  app()
