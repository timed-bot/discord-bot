from typing import Union
import inject
import motor.motor_asyncio

from helpers import singleton

from interfaces.guild import GuildDataclass

from services import GlobalConfigService
from services.database.modules.guilds_module import GuildsModuleService
from services.database.redis_db import RedisDatabaseService


@singleton
class PrimaryDatabaseService():

    @inject.autoparams()
    def __init__(self, config: GlobalConfigService):
        self.__redis_db = RedisDatabaseService(config=config)

        self.__cleint = motor.motor_asyncio.AsyncIOMotorClient(
            config.mongo_connstring)
        self.__db = self.__cleint.get_database('discordbot')
        self.__guilds = self.__db.get_collection('guilds')

        self.__guilds_module = GuildsModuleService(
            self.__guilds, self.__redis_db)

    async def get_guild_config(self, guild_id: str) -> Union[GuildDataclass, None]:
        return await self.__guilds_module.get_guild_config(guild_id)
