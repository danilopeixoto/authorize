from pathlib import Path
from typing import Optional

import typer

from . import __version__


app = typer.Typer(add_completion = False)


def version(value: bool):
  '''Show version and exit.'''

  if value:
    typer.echo(f'Version: {__version__}')
    raise typer.Exit()

@app.command(context_settings = dict(help_option_names = ['-h', '--help']))
def main(
    filename: Path,
    version: Optional[bool] = typer.Option(
      None, '--version', '-v', callback = version, help = version.__doc__)):
  '''Process bank operations.'''

  if not filename.is_file():
    typer.echo(f'Invalid file from {filename.resolve()}.')
    raise typer.Exit(code = 1)

  typer.echo(filename)


if __name__ == '__main__':
  app()
