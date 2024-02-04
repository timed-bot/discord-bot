from dataclasses import dataclass
from typing import Any, List
from datetime import datetime
from dataclasses_json import dataclass_json


@dataclass
@dataclass_json
class CreateEventDTO:
    start_time: datetime
    end_time: datetime
    event_name: str
    roles: List[int]
    scenarios: Any
