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
    RegionNames.KAMUI_EZOFUJI: [
        ExitData(RegionNames.WAWKU_SHRINE, required_items_events=["Kamui (Ezofuiji) - Deliver Lika to Kai"]),
        ExitData(RegionNames.KAMUI_EZOFUJI_PLATFORM, required_items_events=[BrushTechniques.GREENSPROUT_VINE])
    ]
}
events = {
    RegionNames.KAMUI_EZOFUJI: {
        "Kamui (Ezofuiji) - Deliver Lika to Kai": EventData(
            required_items_events=["Moon Cave, 100 years ago - Defeat Orochi Cutscene"]),
        "Kamui (Ezofuiji) - Unlock Mist Warp Point": EventData(),
    },
}
locations = {
    RegionNames.KAMUI_EZOFUJI:{
        "Kamui (Ezofuiji) - Freestanding chest near altar" : LocData(container_check_id(MapIds.KAMUI_EZOFUJI,6))
    },
    RegionNames.KAMUI_EZOFUJI_ROCKY: {
        "Kamui (Ezofuiji) - Left chest in rocky area": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 9)),
        "Kamui (Ezofuiji) - Center chest in rocky area": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 7)),
        "Kamui (Ezofuiji) - Right chest in rocky area": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 8)),
    },
    RegionNames.KAMUI_EZOFUJI_PLATFORM: {
        "Kamui (Ezofuiji) - Flaming chest on westmost platform": LocData(container_check_id(MapIds.KAMUI_EZOFUJI,3),type=LocationType.BURNING_CHEST),
        "Kamui (Ezofuiji) - Frozen chest on westmost platform": LocData(container_check_id(MapIds.KAMUI_EZOFUJI,5),type=LocationType.FROZEN_CHEST_SPECIAL_SOURCE),
        "Kamui (Ezofuiji) - Stone buried chest on northernmost platform": LocData(
            container_check_id(MapIds.KAMUI_EZOFUJI, 13),type=LocationType.STONE_BURIED_CHEST),
        "Kamui (Ezofuiji) - Freestanding chest on northernmost platform": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 16)),
        "Kamui (Ezofuiji) - buried chest on northernmost platform": LocData(
            container_check_id(MapIds.KAMUI_EZOFUJI, 10),type=LocationType.BURIED_CHEST)
    }

}
shop_locations = {

}
warps = {
    RegionNames.KAMUI_EZOFUJI_ROCKY: [
        WarpData(WarpType.MIST_WARP, trigger_warp_to=Has("Kamui (Ezofuiji) - Unlock Mist Warp Point"),
                 trigger_warp_from=True_)
    ]
}
