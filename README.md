# Advent of Code 2024

Puzzles found in [Advent of Code](https://adventofcode.com/2024).

[![AoC Test Run](https://github.com/valies/AoC2024/actions/workflows/tests.yml/badge.svg)](https://github.com/valies/AoC2024/actions/workflows/tests.yml)

## Requirements

This project was made with:
- Python 3.11.11
- pyenv 2.4.21
- pipenv 2024.4.0
- PyCharm 2024.1.2

> [!NOTE]  
> Input files can be retrieved from the Advent of Code website.

### Use pyenv
In case you need to maintain multiple Python versions.

#### 1. Install pyenv
```zsh
brew install pyenv
```

#### 2. Install the necessary python version
```zsh
pyenv install {version}
```
If you need a list of available versions:
```zsh
pyenv install --list
```

#### 3. Set default python version
```zsh
pyenv global {version}
```

### Install via homebrew

In case you only need to maintain one Python version.

#### Install Python via homebrew
```zsh
brew install python
```

### Pipenv

#### 1. Install pipenv
```zsh
brew install pipenv
```

#### 2. Install dependencies
```zsh
pipenv install --dev
```

#### 3. Activate pip env
```zsh
pipenv shell
```

#### 4. Leave pip env
```zsh
exit
```

## Run

_Mind that these commands need to be run in the pip env._

### Run flake8 (style guide)
```zsh
flake8
```

### Run black (PEP8 code formatter)
```zsh
black .
```

### Run isort (sort imports)
```zsh
isort .
```

### Get results
> [!NOTE]
> You need to retrieve your input files from the AoC website and put them in a folder "input" with the names as mentioned in main.py.

```zsh
python main.py
```

### Run tests
```zsh
python -m unittest
```

### Run tests with pytest
```zsh
pytest
```