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
    RegionNames.KAMUI: [
        ExitData(RegionNames.SHINSHU_PLATEAU, one_way=True),
        ExitData(RegionNames.KAMUI_DOJO)
    ]
}
events = {
    RegionNames.KAMUI_DOJO: {
        # Convert these to items at some point when dojos techs/shops are randomizable
        "Kamui - Buy Holy Eagle": EventData(event_item_name="Holy Eagle"),
        "Kamui - Buy Digging Champ": EventData(event_item_name="Digging Champ")
    },
}
locations = {
    RegionNames.KAMUI:
        {
            "Kamui - Buried Chest near Dojo": LocData(container_check_id(MapIds.KAMUI, 6),
                                                      type=LocationType.BURIED_CHEST),
            "Kamui - Buried Chest near central lake": LocData(container_check_id(MapIds.KAMUI, 8),
                                                              type=LocationType.BURIED_CHEST),
            "Kamui - Buried Chest near Yoshpet entrance Left": LocData(container_check_id(MapIds.KAMUI, 12),
                                                                       type=LocationType.BURIED_CHEST),
            "Kamui - Frozen Chest near Dojo": LocData(container_check_id(MapIds.KAMUI, 16),
                                                      type=LocationType.FROZEN_CHEST),
            "Kamui - Frozen Chest near Yoichi's hut": LocData(container_check_id(MapIds.KAMUI, 19),
                                                              type=LocationType.FROZEN_CHEST),
            "Kamui - Buried Chest near Yoshpet entrance Right": LocData(container_check_id(MapIds.KAMUI, 21),
                                                                        type=LocationType.BURIED_CHEST),
            "Kamui - Buried Chest near Kokari's Fishing spot": LocData(container_check_id(MapIds.KAMUI, 22),
                                                                       type=LocationType.BURIED_CHEST),

            # TODO: Check access for these chests
            "Kamui - Freestanding Chest on ice wall": LocData(container_check_id(MapIds.KAMUI, 7)),
            "Kamui - Frozen Chest in bear cave back": LocData(container_check_id(MapIds.KAMUI, 9),
                                                              type=LocationType.FROZEN_CHEST),
            "Kamui - Frozen Chest in bear cave after gap": LocData(container_check_id(MapIds.KAMUI, 11),
                                                                   type=LocationType.FROZEN_CHEST),
            "Kamui - Freestanding chest near ice cascade": LocData(container_check_id(MapIds.KAMUI, 13)),
            "Kamui - Freestanding Chest in bear cave middle pillar": LocData(container_check_id(MapIds.KAMUI, 14)),
            "Kamui - Frozen Chest in bear cave entrance": LocData(container_check_id(MapIds.KAMUI, 15),
                                                                  type=LocationType.FROZEN_CHEST),
            "Kamui - Buried Chest near Yoichi's hut": LocData(container_check_id(MapIds.KAMUI, 20),
                                                              type=LocationType.BURIED_CHEST),
        }
}

warps = {
    # TODO: Add Missing mermaid spring
    RegionNames.CURSED_KAMUI_PRE_FIGHT: [
        WarpData(WarpType.MIST_WARP, Has("Kamui - Unlock mist warp point"), Has("Kamui - Unlock mist warp point"))
    ]
}
