from dataclasses import dataclass

from dataclasses_json import dataclass_json

from interfaces.guild_config import GuildConfigDataclass


@dataclass
@dataclass_json
class GuildDataclass:
    config: GuildConfigDataclass
