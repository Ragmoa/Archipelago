from typing import TYPE_CHECKING

from rule_builder.rules import True_, Has
from ..CheckIds import container_check_id, shop_check_id
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames, MapIds
from ..Enums.WarpType import WarpType
from ..Types import ExitData, EventData, WarpData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.INNER_YOSHPET_ENTRANCE: [
        ExitData(RegionNames.YOSHPET_MIDDLE, one_way=True),
        ExitData(RegionNames.INNER_YOSHPET_1_1),
    ]
}
events = {
}
locations = {
}
