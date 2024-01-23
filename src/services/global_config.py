'''
This module is responsible for reading the global config file and returning the bot token.
'''

import json
from typing import Dict, Literal
from os import path

from helpers import singleton


@singleton
class GlobalConfigService():
    '''
    This class is responsible for reading the global config file and returning the bot token.
    '''

    def __init__(self, basedir: str, env: Literal["dev", "prod"]):
        '''
        Initializes the file path.
        '''

        self.__data: Dict[str, any] = {}
        self.__basedir = basedir
        self.__env = env
        self.__file_path = path.join(self.__basedir, f'{env}.env.json')

        with open(self.__file_path, encoding='UTF-8') as file:
            self.__data = json.load(file)

    @property
    def bot_token(self):
        '''
        Returns the bot token from the config file.
        '''
        return self.__data['bot_token']

    @property
    def default_prefix(self):
        '''
        Returns the default prefix from the config file.
        '''
        return self.__data.get('bot_prefix', '>')

    @property
    def mongo_connstring(self):
        '''
        Returns the default prefix from the config file.
        '''
        return self.__data['mongo_connstring']

    @property
    def redis_host(self):
        '''
        Returns the default prefix from the config file.
        '''
        return self.__data['redis_host']

    @property
    def redis_port(self):
        '''
        Returns the default prefix from the config file.
        '''
        return self.__data['redis_port']

    @property
    def data(self):
        '''
        Returns the data from the config file.
        '''
        return self.__data

    @property
    def config_path(self):
        '''
        Returns the file path.
        '''
        return self.__file_path

    @property
    def basedir(self):
        '''
        Returns the basedir.
        '''
        return self.__basedir

    @property
    def env(self):
        '''
        Returns the env.
        '''
        return self.__env
