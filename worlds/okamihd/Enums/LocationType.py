from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import OkamiWorld


class LocationType(Enum):
    FREESTANDING_ITEM=0,
    NORMAL_CHEST=1,
    UNDERWATER_CHEST=2,
    TREASURE_BUD=3,
    BURNING_CHEST=4,
    BURIED_CHEST=5,
    STONE_BURIED_CHEST=6,
    CONSTELLATION=7,
    BURIED_UNDER_LEAF_PILE=8,
    EVENT=9
    BURNING_CHEST_NO_WATER=10,
