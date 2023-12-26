from os import path
import json

class GlobalConfigService(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_bot_token(self):
        with open(self.file_path) as file:
            data = json.load(file)
            return data.get('bot_token')

    
    
