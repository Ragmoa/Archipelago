from typing import TYPE_CHECKING

from rule_builder.rules import True_, Has
from ..CheckIds import shop_check_id
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames
from ..Enums.WarpType import WarpType
from ..Types import ExitData, EventData, WarpData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.CURSED_KAMUI_PRE_FIGHT: [
        ExitData(RegionNames.CURSED_KAMUI, required_items_events=["Kamui - Fight Oki"], one_way=True)
    ],
    RegionNames.CURSED_KAMUI: [
        ExitData(RegionNames.KAMUI, required_items_events=["Kamui - Bloom Guardian Sapling"], one_way=True)
    ],
}
events = {
    RegionNames.CURSED_KAMUI_PRE_FIGHT: {
        "Kamui - Unlock mist warp point": EventData(),
        "Kamui - Mandatory Namahage Fight at entrance": EventData(
            mandatory_enemies=[OkamiEnemies.NAMAHAGE, OkamiEnemies.BLADE_NAMAHAGE]),
        "Kamui - Fight Oki": EventData(mandatory_enemies=[OkamiEnemies.OKI],
                                       required_items_events=["Kamui - Mandatory Namahage Fight at entrance"])
    },
    RegionNames.CURSED_KAMUI: {
        "Kamui - Blow up guardian sapling rock": EventData(required_brush_techniques=[BrushTechniques.THUNDERSTORM]),
        "Kamui - Bloom Guardian Sapling": EventData(required_items_events=["Kamui - Blow up guardian sapling rock"],
                                                    required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM])
    }
}
locations = {
}
# TODO: Check if this merchant is avilable from cursed
shop_locations = {
    RegionNames.CURSED_KAMUI: {
        "Kamui - Shop Slot 1": LocData(shop_check_id(7, 0), type=LocationType.SHOP),
        "Kamui - Shop Slot 2": LocData(shop_check_id(7, 1), type=LocationType.SHOP),
        "Kamui - Shop Slot 3": LocData(shop_check_id(7, 2), type=LocationType.SHOP),
        "Kamui - Shop Slot 4": LocData(shop_check_id(7, 3), type=LocationType.SHOP),
        "Kamui - Shop Slot 5": LocData(shop_check_id(7, 4), type=LocationType.SHOP),
        "Kamui - Shop Slot 6": LocData(shop_check_id(7, 5), type=LocationType.SHOP),
        "Kamui - Shop Slot 7": LocData(shop_check_id(7, 6), type=LocationType.SHOP),
        "Kamui - Shop Slot 8": LocData(shop_check_id(7, 7), type=LocationType.SHOP),
        "Kamui - Shop Slot 9": LocData(shop_check_id(7, 8), type=LocationType.SHOP),
        "Kamui - Shop Slot 10": LocData(shop_check_id(7, 9), type=LocationType.SHOP),
        "Kamui - Shop Slot 11": LocData(shop_check_id(7, 10), type=LocationType.SHOP),
        "Kamui - Shop Slot 12": LocData(shop_check_id(7, 11), type=LocationType.SHOP),
    }
}

warps = {
    RegionNames.CURSED_KAMUI_PRE_FIGHT: [
        WarpData(WarpType.MIST_WARP, True_, Has("Kamui - Unlock mist warp point"))
    ]
}
