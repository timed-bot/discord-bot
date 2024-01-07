'''
This module is responsible for reading the global config file and returning the bot token.
'''

import json

class GlobalConfigService(object):
    '''
    This class is responsible for reading the global config file and returning the bot token.
    '''
    def __init__(self, file_path):
        self.file_path = file_path

    def get_bot_token(self):
        '''
        Returns the bot token from the config file.
        '''
        with open(self.file_path, encoding='UTF-8') as file:
            data = json.load(file)
            return data.get('bot_token')
    
    
    
