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
    RegionNames.ARK_OF_YAMATO: [
        ExitData(RegionNames.ARK_OF_YAMATO_YAMI, one_way=True,
                 required_items_events=["Ark of Yamato - Defeat Spider Queen", "Ark of Yamato - Defeat Orochi",
                                        "Ark of Yamato - Defeat Blight", "Ark of Yamato - Defeat Blight",
                                        "Ark of Yamato - Defeat Crimson Helm"]),
        ExitData(RegionNames.ARK_OF_YAMATO_NINETAILS, one_way=True),
        ExitData(RegionNames.ARK_OF_YAMATO_CRIMSON, one_way=True),
        ExitData(RegionNames.ARK_OF_YAMATO_SPIDER, one_way=True),
        ExitData(RegionNames.ARK_OF_YAMATO_OROCHI, one_way=True),
        ExitData(RegionNames.ARK_OF_YAMATO_BLIGHT, one_way=True)
    ]
}
events = {
}
locations = {

}
