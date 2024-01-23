from services import GlobalConfigService
from helpers import singleton


@singleton
class EventsService(object):
    def __init__(self, config: GlobalConfigService): ...
