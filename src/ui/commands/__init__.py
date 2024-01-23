import inject
from services import GlobalConfigService

__globalConfigService: GlobalConfigService = inject.instance(
    GlobalConfigService)

if __globalConfigService.env == 'dev':
    from .commands_dev import *
elif __globalConfigService.env == 'prod':
    from .commands_prod import *
