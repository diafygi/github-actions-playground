```
# install dependencies in virtual environment
virtualenv -p python3 /tmp/gavenv3
source /tmp/gavenv3/bin/activate
pip install -U -r tests/requirements.txt

# run tests with coverage
coverage erase
coverage run --source . --omit ./setup.py -m unittest tests
coverage report -m
coverage html
```

