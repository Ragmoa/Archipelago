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
    RegionNames.SHINSHU_100_PRE_CLAY: [
        ExitData(RegionNames.KAMIKI_100, one_way=True),
        ExitData(RegionNames.SHINSHU_100_CLAY, one_way=True, loading_screen=False),
    ],
    RegionNames.SHINSHU_100_CLAY: [
        ExitData(RegionNames.SHINSHU_100, one_way=True, loading_screen=False,
                 required_items_events=["Shinshu Field, 100 years ago - Mandatory Fight at Kamiki entrance"]),
        ExitData(RegionNames.SHINSHU_100_PRE_CLAY, one_way=True, loading_screen=False,
                 required_items_events=["Shinshu Field, 100 years ago - Mandatory Fight at Kamiki entrance"])

    ],
    RegionNames.SHINSHU_100: [
        ExitData(RegionNames.SHINSHU_100_CLAY, one_way=True, loading_screen=False),
        ExitData(RegionNames.MOON_CAVE_100_OUTSIDE),
    ]
}
events = {
    RegionNames.SHINSHU_100_CLAY: {
        "Shinshu Field, 100 years ago - Mandatory Fight at Kamiki entrance": EventData(
            mandatory_enemies=[OkamiEnemies.CLAY_SAMURAI, OkamiEnemies.CLAY_SOLDIER])
    }
}
locations = {
    RegionNames.SHINSHU_100: {
        "Shinshu Field, 100 years ago - Buried chest in Sun Drawing": LocData(
            container_check_id(MapIds.SHINSHU_100, 12)),
        "Shinshu Field, 100 years ago - Freestanding chest on ledge near dojo lake": LocData(
            container_check_id(MapIds.SHINSHU_100, 10)),
        "Shinshu Field, 100 years ago - Freestanding chest after crossing Torii": LocData(
            container_check_id(MapIds.SHINSHU_100, 0)),
        "Shinshu Field, 100 years ago - Freestanding chest near lake Harami's edge": LocData(
            container_check_id(MapIds.SHINSHU_100, 7))
    }
}
