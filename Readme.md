# Lambda template

This is a template for a monorepo lambda project

# VScode

This project has to be opened a VScode `workspace` because specific configurations to run tests and code analysis

## Init

To initialize the python environment run:

    make init

This will install the python environment (managed by `pipenv`) and create a `.env` file

## Run tests

The tests can be run in command-line

    make run_tests

or installing a VSCode extension by pressing `Ctrl + P` or `Cmd + P` and inputting:

    ext install LittleFoxTeam.vscode-python-test-adapter
