# An opinionated example project in Python

## Features

- Poetry
- `src` layout
- Flake8 + Black
- pytest
- config file for logging

## Setup virtual environment

With the `venv` module:

```bash
python3 -m venv venv
source venv/bin/activate
```

With the `pyenv`

```bash
pyenv virtualenv 3.8.3 my-venv
pyenv local my-venv
```

## Do further setup with poetry

Note that running `poetry install` is to install dependencies, but it's **also to recognize `src` directory**.

```bash
pip install -U pip
poetry install # to install dependencies, recognize src directory, and update scripts
poetry hello
```

## Run tests

```bash
pytest
```

## Run scripts

```bash
poetry run hello
python src/main.py
```

## Example VS Code configuration

`settings.json`:

```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false
}
```


## References

- https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
- https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260#0435
- https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80
- https://hynek.me/articles/testing-packaging/
