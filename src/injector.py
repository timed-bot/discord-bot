from sys import argv
from os import path

import inject

from services import GlobalConfigService, JobsService, PrimaryDatabaseService, EventsService


def injector_config(binder: inject.Binder):
    binder.bind_to_constructor(
        'env', lambda: argv[1] if len(argv) > 1 else 'dev')
    binder.bind(GlobalConfigService, GlobalConfigService(path.dirname(path.abspath(__file__)), argv[1] if len(
        argv) > 1 else 'dev'))

    binder.bind_to_provider(JobsService, lambda: JobsService(
        inject.instance(GlobalConfigService)))
    binder.bind_to_provider(PrimaryDatabaseService, lambda: PrimaryDatabaseService(
        inject.instance(GlobalConfigService)))
    binder.bind_to_provider(EventsService, lambda: EventsService(
        inject.instance(GlobalConfigService)))
