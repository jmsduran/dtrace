![Python application](https://github.com/jmsduran/dtrace/workflows/Python%20application/badge.svg)

# dtrace
Python ray tracer.

## Build & Test

If venv is not installed:
```
sudo apt-get install python3-venv
```

To setup, from the project's root directory:
```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

To run tests and linter, from project's root directory:
```
pytest
flake8 src/
```
