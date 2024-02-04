from dataclasses import dataclass
from typing import Any, List

from dataclasses_json import dataclass_json

from interfaces.guild_config import GuildConfigDataclass


@dataclass
@dataclass_json
class GuildDataclass:
    config: GuildConfigDataclass
    events: List[Any]
