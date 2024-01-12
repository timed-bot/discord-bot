'''
This is the main entry point of the bot.
'''
import sys
import os
import inject

from services import GlobalConfigService

from injector import injector_config
inject.configure(injector_config)


if __name__ == '__main__':
    from bot import create_bot

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    GlobalConfig: GlobalConfigService = inject.instance(GlobalConfigService)

    if GlobalConfig.env == 'dev':
        bot = create_bot()
        bot.run(GlobalConfig.bot_token)
