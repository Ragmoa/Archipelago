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
    RegionNames.WEP_KEER:[
        ExitData(RegionNames.WEP_KEER_MERCHANT,one_way=True,loading_screen=False,required_items_events=["Wep'keer - Meet Kemu"]),
        ExitData(RegionNames.WEP_KEER_SQUARE,one_way=True,required_items_events=["Wep'keer - Meet Kemu"]),
        ExitData(RegionNames.KAMUI_EZOFUJI, required_items_events=["Wep'keer - Meet Kemu"])
    ]
}
events = {
    RegionNames.WEP_KEER:{
        "Wep'keer - Unlock Mist Warp Point":EventData(),
        "Wep'keer - Meet Kemu": EventData()
    }
}
locations = {
    RegionNames.WEP_KEER:{
        "Wep'keer - Buried Chest near south waterfall ledge":LocData(container_check_id(MapIds.WEP_KEER,1),type=LocationType.BURIED_CHEST),
        "Wep'keer - Buried Chest near Squirrel girl's house ":LocData(container_check_id(MapIds.WEP_KEER,3),type=LocationType.BURIED_CHEST),
        "Wep'keer - Buried Chest house right of merchant":LocData(container_check_id(MapIds.WEP_KEER,4),type=LocationType.BURIED_CHEST),
        "Wep'keer - Freestanding Chest in bear nook": LocData(container_check_id(MapIds.WEP_KEER, 5)),
        "Wep'keer - Buried Chest near on ledge above square entrance": LocData(container_check_id(MapIds.WEP_KEER, 7),type=LocationType.BURIED_CHEST),
        "Wep'keer - Freestanding chest under bridge behind Kai's house ": LocData(container_check_id(MapIds.WEP_KEER, 9)),
        "Wep'keer - Buried chest near bears outside Kemu's house ": LocData(
            container_check_id(MapIds.WEP_KEER, 10)),
    }
}

shop_locations = {
    RegionNames.WEP_KEER_MERCHANT: {
        "Wep'keer - Shop Slot 1": LocData(shop_check_id(21, 0), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 2": LocData(shop_check_id(21, 1), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 3": LocData(shop_check_id(21, 2), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 4": LocData(shop_check_id(21, 3), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 5": LocData(shop_check_id(21, 4), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 6": LocData(shop_check_id(21, 5), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 7": LocData(shop_check_id(21, 6), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 8": LocData(shop_check_id(21, 7), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 9": LocData(shop_check_id(21, 8), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 10": LocData(shop_check_id(21, 9), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 11": LocData(shop_check_id(21, 10), type=LocationType.SHOP),
        "Wep'keer - Shop Slot 12": LocData(shop_check_id(21, 11), type=LocationType.SHOP),
    }
}
warps={
    RegionNames.WEP_KEER:[
        WarpData(WarpType.MIST_WARP,True_,Has("Wep'keer - Unlock Mist Warp Point"))
    ]
}