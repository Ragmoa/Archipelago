from typing import TYPE_CHECKING

from rule_builder.rules import True_, Has
from ..CheckIds import container_check_id, shop_check_id
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames, MapIds
from ..Enums.WarpType import WarpType
from ..Rules import long_swim_rule
from ..Types import ExitData, EventData, WarpData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.KAMIKI_100:[
        ExitData(RegionNames.KAMIKI_100_ISLANDS,special_rule=long_swim_rule,loading_screen=False),
        ExitData(RegionNames.SHINSHU_100_PRE_CLAY, one_way=True, required_items_events=["Kamiki Village, 100 years ago - Steal Nami's Robe"])
    ]
}
events = {
    RegionNames.KAMIKI_100:{
        "Kamiki Village, 100 years ago - Defeat Nagi" : EventData(mandatory_enemies=[OkamiEnemies.NAGI]),
        "Kamiki Village, 100 years ago - Steal Nami's Robe" : EventData(required_items_events=["Kamiki Village, 100 years ago - Defeat Nagi"])
    }
}
locations = {
    RegionNames.KAMIKI_100: {
        "Kamiki Village, 100 years ago - Buried chest behind Grapefruit's house": LocData(
            container_check_id(MapIds.KAMIKI_100, 41)),
        "Kamiki Village, 100 years ago - Underwater chest in river, near Lake 1": LocData(
            container_check_id(MapIds.KAMIKI_100, 42),type=LocationType.UNDERWATER_CHEST),
        "Kamiki Village, 100 years ago - Underwater chest in river, near Lake 2": LocData(
            container_check_id(MapIds.KAMIKI_100, 43),type=LocationType.UNDERWATER_CHEST),
        "Kamiki Village, 100 years ago - Underwater near Laundry Pole": LocData(
            container_check_id(MapIds.KAMIKI_100, 44),type=LocationType.UNDERWATER_CHEST),
    },
    RegionNames.KAMIKI_100_ISLANDS:{
        "Kamiki Village, 100 years ago - Buried chest on eastmost Island, behind rock": LocData(
            container_check_id(MapIds.KAMIKI_100, 40)),
    }
}

shop_locations = {
    RegionNames.KAMIKI_100:{
        "Kamiki Village, 100 years ago - Shop Slot 1": LocData(shop_check_id(6, 0), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 2": LocData(shop_check_id(6, 1), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 3": LocData(shop_check_id(6, 2), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 4": LocData(shop_check_id(6, 3), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 5": LocData(shop_check_id(6, 4), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 6": LocData(shop_check_id(6, 5), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 7": LocData(shop_check_id(6, 6), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 8": LocData(shop_check_id(6, 7), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 9": LocData(shop_check_id(6, 8), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 10": LocData(shop_check_id(6, 9), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 11": LocData(shop_check_id(6, 10), type=LocationType.SHOP),
        "Kamiki Village, 100 years ago - Shop Slot 12": LocData(shop_check_id(6, 11), type=LocationType.SHOP),
    }
}
