from typing import Any, Union
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

    async def get_guild(self, guild_id: int) -> Union[GuildDataclass, None]:
        raw_guild: bytes = await self.__redis_client.get(f'{GUILD_KEY}:{guild_id}')
        if raw_guild:
            return GuildDataclass.from_json(raw_guild.decode('UTF-8'))
        else:
            return None

    async def create_guild(self, guild_id: int):
        await self.__redis_client.set(f'{GUILD_KEY}:{guild_id}', '{}')

    async def add_event(self, guild_id: int, dto: Any) -> GuildDataclass:
        raw_guild = await self.__redis_client.get(f'{GUILD_KEY}:{guild_id}')
        guild: GuildDataclass = GuildDataclass.from_json(
            raw_guild.decode('UTF-8'))
        guild.events.append(dto)
        await self.__redis_client.set(f'{GUILD_KEY}:{guild_id}', guild.to_json())
        return guild

    async def remove_event(self, guild_id: int, event_id: int) -> GuildDataclass:
        raw_guild = await self.__redis_client.get(f'{GUILD_KEY}:{guild_id}')
        guild: GuildDataclass = GuildDataclass.from_json(
            raw_guild.decode('UTF-8'))
        guild.events = list(filter(lambda x: x._id != event_id, guild.events))

        await self.__redis_client.set(f'{GUILD_KEY}:{guild_id}', guild.to_json())
        return guild
