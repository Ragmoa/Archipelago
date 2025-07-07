from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import OkamiWorld


class LocationType(Enum):
    FREESTANDING_ITEM=0,
    NORMAL_CHEST=1,
    UNDERWATRER_CHEST=2,
    TREASURE_BUD=3,
    BURNING_CHEST=4,
    BURIED_CHEST=5,
    STONE_BURIED_CHEST=6,
