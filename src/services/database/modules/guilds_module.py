from typing import Union
from pymongo.collection import Collection

from helpers import singleton
from services.database.redis_db import RedisDatabaseService

from interfaces import GuildDataclass


@singleton
class GuildsModuleService():
    def __init__(self, collection: Collection, redis_db: RedisDatabaseService) -> None:
        self.__redis_db = redis_db
        self.__guilds = collection

    async def __try_get_guild_from_cache(self, guild_id) -> Union[GuildDataclass, None]:
        return await self.__redis_db.get_guild(guild_id)

    async def __register_guild(self, guild_id):
        guild = await self.__guilds.find_one({'_id': guild_id})
        if not guild:
            await self.__redis_db.create_guild(guild_id)
            return await self.__guilds.insert_one({'_id': guild_id, 'config': {}})
        else:
            return guild

    async def get_guild_config(self, guild_id: str) -> Union[GuildDataclass, None]:
        guild: GuildDataclass = await self.__try_get_guild_from_cache(guild_id)
        if not guild:
            guild: GuildDataclass = await self.__guilds.find_one({'_id': guild_id})
            if not guild:
                await self.__register_guild(guild_id)
                return None

        return guild
