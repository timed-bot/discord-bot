from json import loads
from typing import Any, Dict, Union
from aredis import StrictRedis

from services import GlobalConfigService
from helpers import singleton

from interfaces import GuildDataclass

GUILD_KEY = 'guilds'


@singleton
class RedisDatabaseService():
    def __init__(self, config: GlobalConfigService):
        self.__redis_client = StrictRedis(
            host=config.redis_host, port=config.redis_port, db=0)

    async def get_guild(self, guild_id) -> Union[GuildDataclass, None]:
        raw_guild: bytes = await self.__redis_client.get(f'{GUILD_KEY}:{guild_id}')
        if raw_guild:
            json_guild: Dict[str: Any] = loads(raw_guild.decode('UTF-8'))
            return GuildDataclass.from_json(json_guild)
        else:
            return None

    async def create_guild(self, guild_id):
        await self.__redis_client.set(f'{GUILD_KEY}:{guild_id}', '{}')
