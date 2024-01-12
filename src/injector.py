from sys import argv
from os import path

import inject

from services import GlobalConfigService


def injector_config(binder: inject.Binder):
    binder.bind(GlobalConfigService, GlobalConfigService(path.dirname(path.abspath(__file__)), argv[1] if len(
        argv) > 1 else 'dev'))
