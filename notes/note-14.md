# CS2 Spring 2025 Note 14

## Unit testing

According to [this](https://en.wikipedia.org/wiki/Unit_testing) Wikipedia
article, unit testing is

> a form of [software
> testing](https://github.com/alainkaegi/pythonorama/blob/main/software_development/testing.md)
> by which isolated source code is tested to validate expected behavior.

## `pytest`

There are many unit testing frameworks.  We will be using `pytest`.

### Conventions

Any file whose name ends with `_test` is assumed to contain your test code.

Any function whose name starts with `test_` is assumed to be a (single) unit
test.

Test functions typically call the function `assert` to check the behavior of the
function being tested.

### Process

When you open any test files (ending with `_test`), a beaker icon should appear
on the left-hand side of the Visual Studio Code application.  Clicking on the
beaker icon guides you through some configuration steps (framework: `pytest`,
directory: `.`).  At this point `pytest` looks for all functions starting with
`test_`, lists them in an explorer pane, and gives you options to run all the
tests at once or one particular test at a time.
