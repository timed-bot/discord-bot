

py -m pip install pipenv
py -m pipenv install
py -m pipenv run py -m pylint --recursive=y ./src
py -m pipenv run py ./src/start.py dev