![Python application](https://github.com/jmsduran/dtrace/workflows/Python%20application/badge.svg)

# dtrace
Python ray tracer.

## Build & Test
To setup, from the project's root directory:
```
sudo apt-get install python3-venv
python3 -m venv dtrace-env
source dtrace-env/bin/activate
pip install -r requirements.txt
```

To run tests and linter, from project's root directory:
```
pytest
flake8 ./
```
