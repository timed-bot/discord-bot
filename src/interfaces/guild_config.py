
from typing import Union

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass
@dataclass_json
class GuildConfigDataclass:
    custom_prefix: Union[None, str] = field(default=None)
