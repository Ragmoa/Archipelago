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

}
events = {
    RegionNames.ARK_OF_YAMATO_YAMI: {
        "Ark of Yamato - Defeat Yami": EventData(
            mandatory_enemies=[OkamiEnemies.YAMI_RED, OkamiEnemies.YAMI_BLUE, OkamiEnemies.YAMI_HAND,
                               OkamiEnemies.YAMI_GREEN, OkamiEnemies.YAMI_YELLOW])
    }
}
locations = {

}
