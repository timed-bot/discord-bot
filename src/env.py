'''Environment variables for the application.'''

from os import path

BASE_PATH = path.dirname(path.abspath(__file__))

def config_path(env):
    ''' Returns the path to the config file for the given environment. '''
    return path.join(BASE_PATH, f'{env}.env.json')
