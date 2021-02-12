from pathlib import Path

from distutils.util import convert_path
from setuptools import setup, find_packages


def get_package_info(relative_path):
  '''Get package information from module path.'''

  package_info = {}

  with open(convert_path(Path(relative_path) / '__init__.py'), 'r') as file:
    exec(file.read(), package_info)

  return package_info


package_name = 'authorize'
package_info = get_package_info(package_name)

requirements = [
  'typer>=0.3.0',
  'pydantic>=1.7.0'
]

test_requirements = [
  'pytest>=6.2.0'
]

entrypoints = {
  'console_scripts': [
    f'{package_name} = {package_name}.cli.__main__:app'
  ]
}

setup(
  name = package_name,
  version = package_info['__version__'],
  description = package_info['__description__'],
  author = package_info['__author__'],
  author_email = package_info['__email__'],
  license = package_info['__license__'],
  python_requires = '>=3.6.0',
  install_requires = requirements,
  extras_require = dict(test = test_requirements),
  packages = find_packages(),
  entry_points = entrypoints,
  zip_safe = False)
