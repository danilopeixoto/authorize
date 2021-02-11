# Authorize

Authorizer for bank transactions.

## Prerequisites

* [Python (>=3.6.0)](https://www.python.org)

## Installation

### Production

Install package:

```
pip install .
```

### Development

Install package and test dependencies:

```
pip install .[test]
```

Use the `-e, --editable` flag to install package in development mode.

## Usage

Run application:

```
authorize < data/operations
```

Run `authorize --help` for more information.


## Test

Run tests:

```
pytest
```

> **Note:** requires test dependencies.

## Container image

### Prerequisites

* [Docker Engine (>=19.03.10)](https://www.docker.com)

### Installation

Build container image:

```
docker build -t authorize:1.0.0 .
```

### Usage

Run image application:

```
docker run authorize:1.0.0 < data/operations
```

## Documentation

Check the [documentation](docs/index.md) for architecture and design choices.

## Copyright and license

Copyright (c) 2021, Nu Pagamentos S.A. All rights reserved.

Project developed under a [Proprietary License](LICENSE.md).
