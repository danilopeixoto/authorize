# Architecture and design choices

The architecture has been designed to be modular and extensible for new commands, operations and rules.

Operations are defined as controllers and resolve the rule validation flow and implement the business logic of the operations.

## Models

The requirements do not enforce validation, but Pydantic was used to define the application data model. These strict models provide out of box, parsing, validation and immutability.

They simplify the implementation of the parser and enable the conversion of data into different representations such as the JSON string into native dictionaries.

Null objects are avoided to maintain the consistency of the dataflow. The `UninitializedAccount` model defines the default account properties. While the type distinguishes the state of the account, the data remain exchangeable with the initialized `Account` model.

## Controllers

The design of controllers and rules avoids conditional checks and makes them generally applied to the data.

In order to add a new operation, the `OperationController` interface must be derived. The controllers will be automatically instantiated by the parser based on the name and no additional steps are required to register new operations.

Rules are defined as controller methods decorated/wrapped with `Validator` objects. These objects are collected during the validation step and applied to the data sequentially, returning possible violations.

## States

States are designed to be persistent and mutable structures, providing storage, initialization and updates for model instances. The `AccountState` provides methods for managing bank accounts and related transactions.

## CLI

The application is represented as a CLI. The command line interface documents itself for the end user and new commands can be easily added as new states are implemented in the application.

## Tests

Unit and integrated tests around component groups at different implementation levels, reduce non-logic errors that are hard to debug at the development stage. In the long term, they ensure that refactoring issues are tracked directly and independently.

Functional tests available in the `test_cli` module validate the CLI and test the basic usability of the application.

Pytest has the “fixture” concept that allows to reuse input objects for test routines. It contributes to reduce the test code, but introduces dependence on test inputs that can be hard to track. The feature was regarded as valid because the test was designed to be immutable and incremental.

## Distribution

The application is distributed as a standard Python package that can be easily installed by the PIP package manager. The setup automatically builds binaries for CLI and provides the core library for test development.

The ability to switch between development and production environments allows for fast coding and maintains the integrity of the end product by avoiding the distribution of unnecessary dependencies.

The package also provides a containerized version of the application. The isolation allows to run the application serverless.
