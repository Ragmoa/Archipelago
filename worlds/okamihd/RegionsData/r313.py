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
    RegionNames.WEP_KEER_SQUARE:[
        ExitData(RegionNames.WEP_KEER,one_way=True)
    ]
}
events = {
}
locations = {
    RegionNames.WEP_KEER_SQUARE:{
        "Wep'keer Square - Northern East Side Frozen Chest":LocData(container_check_id(MapIds.WEP_KEER_SQUARE,1),type=LocationType.FROZEN_CHEST),
        "Wep'keer Square - Southern East Side Frozen Chest": LocData(container_check_id(MapIds.WEP_KEER_SQUARE, 2),
                                                                     type=LocationType.FROZEN_CHEST),
        "Wep'keer Square - Southmost Buried Chest": LocData(container_check_id(MapIds.WEP_KEER_SQUARE, 0),
                                                                     type=LocationType.BURIED_CHEST),
        "Wep'keer Square - West Frozen Chest": LocData(container_check_id(MapIds.WEP_KEER_SQUARE, 3),
                                                            type=LocationType.FROZEN_CHEST)
    }
}