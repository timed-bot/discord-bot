from os import path

ENV = 'dev'
BASE_PATH = path.dirname(path.abspath(__file__))
CONFIG_PATH = path.join(BASE_PATH, f'{ENV}.env.json')