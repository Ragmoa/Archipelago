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
    RegionNames.ARK_OF_YAMATO_OROCHI:[
        ExitData(RegionNames.ARK_OF_YAMATO,one_way=True,required_items_events=["Ark of Yamato - Defeat Orochi"])
    ]
}
events = {
    RegionNames.ARK_OF_YAMATO_OROCHI:{
        "Ark of Yamato - Defeat Orochi": EventData(mandatory_enemies=[OkamiEnemies.OROCHI_2])
    }
}
locations = {

}
