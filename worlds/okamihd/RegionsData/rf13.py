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
        ExitData(RegionNames.WAWKU_SHRINE_1F_CANONS, required_items_events=["Kamui (Ezofuji) - Deliver Lika to Kai"]),
        ExitData(RegionNames.KAMUI_EZOFUJI_PLATFORM, required_items_events=[BrushTechniques.GREENSPROUT_VINE]),
        ExitData(RegionNames.KAMUI_EZOFUJI_PS3_CAVE, required_items_events=["Kamui (Ezofuji) - Open PS3 Cave"])
    ]
}
events = {
    RegionNames.KAMUI_EZOFUJI: {
        "Kamui (Ezofuji) - Deliver Lika to Kai": EventData(
            required_items_events=["Moon Cave, 100 years ago - Defeat Orochi Cutscene"]),
        "Kamui (Ezofuji) - Unlock Mist Warp Point": EventData(),
        "Kamui (Ezofuji) - Open PS3 Cave": EventData(power_slash_level=2)
    },
}
locations = {
    RegionNames.KAMUI_EZOFUJI: {
        "Kamui (Ezofuji) - Freestanding chest near altar": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 6))
    },
    RegionNames.KAMUI_EZOFUJI_ROCKY: {
        "Kamui (Ezofuji) - Left chest in rocky area": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 9)),
        "Kamui (Ezofuji) - Center chest in rocky area": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 7)),
        "Kamui (Ezofuji) - Right chest in rocky area": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 8)),
    },
    RegionNames.KAMUI_EZOFUJI_PLATFORM: {
        "Kamui (Ezofuji) - Flaming chest on westmost platform": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 3),
                                                                        type=LocationType.BURNING_CHEST),
        "Kamui (Ezofuji) - Frozen chest on westmost platform": LocData(container_check_id(MapIds.KAMUI_EZOFUJI, 5),
                                                                       type=LocationType.FROZEN_CHEST_SPECIAL_SOURCE),
        "Kamui (Ezofuji) - Stone buried chest on northernmost platform": LocData(
            container_check_id(MapIds.KAMUI_EZOFUJI, 13), type=LocationType.STONE_BURIED_CHEST),
        "Kamui (Ezofuji) - Freestanding chest on northernmost platform": LocData(
            container_check_id(MapIds.KAMUI_EZOFUJI, 16)),
        "Kamui (Ezofuji) - buried chest on northernmost platform": LocData(
            container_check_id(MapIds.KAMUI_EZOFUJI, 10), type=LocationType.BURIED_CHEST)
    }

}
warps = {
    RegionNames.KAMUI_EZOFUJI_ROCKY: [
        WarpData(WarpType.MIST_WARP, trigger_warp_to=Has("Kamui (Ezofuji) - Unlock Mist Warp Point"),
                 trigger_warp_from=True_)
    ]
}
