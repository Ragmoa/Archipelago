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
        ExitData(RegionNames.KAMUI_DOJO),
        ExitData(RegionNames.KAMUI_IGLOO_FIGHT, one_way=True, loading_screen=False)
    ],
    RegionNames.KAMUI_IGLOO_FIGHT: [
        ExitData(RegionNames.KAMUI, one_way=True, loading_screen=False,
                 required_items_events=["Kamui - Mandatory Igloo Turtle Fight"]),
        ExitData(RegionNames.KAMUI_NORTHERN, one_way=True, loading_screen=False,
                 required_items_events=["Kamui - Mandatory Igloo Turtle Fight"]),
    ],
    RegionNames.KAMUI_NORTHERN: [
        ExitData(RegionNames.KAMUI_IGLOO_FIGHT, one_way=True, loading_screen=False),
        ExitData(RegionNames.WEP_KEER)
    ]
}
events = {
    RegionNames.KAMUI_DOJO: {
        # Convert these to items at some point when dojos techs/shops are randomizable
        "Kamui - Buy Holy Eagle": EventData(event_item_name="Holy Eagle"),
        "Kamui - Buy Digging Champ": EventData(event_item_name="Digging Champ")
    },
    RegionNames.KAMUI_IGLOO_FIGHT: {
        "Kamui - Mandatory Igloo Turtle Fight": EventData(mandatory_enemies=[OkamiEnemies.IGLOO_TURTLE])
    },
    RegionNames.KAMUI_NORTHERN: {
        "Kamui - Clear lake cursed torii": EventData(
            mandatory_enemies=[OkamiEnemies.BLADE_NAMAHAGE, OkamiEnemies.BUCKET_NAMAHAGE])
    }
}
locations = {
    RegionNames.KAMUI_NORTHERN: {
        "Kamui - Buried Chest near central lake": LocData(container_check_id(MapIds.KAMUI, 8),
                                                          type=LocationType.BURIED_CHEST),
        "Kamui - Buried Chest near Yoshpet entrance Left": LocData(container_check_id(MapIds.KAMUI, 12),
                                                                   type=LocationType.BURIED_CHEST),
        "Kamui - Buried Chest near Yoshpet entrance Right": LocData(container_check_id(MapIds.KAMUI, 21),
                                                                    type=LocationType.BURIED_CHEST),
        "Kamui - Buried Chest near Mermaid Spring": LocData(container_check_id(MapIds.KAMUI, 20),
                                                            type=LocationType.BURIED_CHEST),
        "Kamui - Freestanding chest on ice cascade lower": LocData(container_check_id(MapIds.KAMUI, 7)),

        "Kamui - Frozen Chest in bear cave entrance": LocData(container_check_id(MapIds.KAMUI, 15),
                                                              type=LocationType.FROZEN_CHEST),

        "Kamui - Frozen Chest in bear cave back": LocData(container_check_id(MapIds.KAMUI, 9),
                                                          type=LocationType.FROZEN_CHEST,
                                                          required_items_events=["Holy Eagle"]),
        "Kamui - Frozen Chest in bear cave after gap": LocData(container_check_id(MapIds.KAMUI, 11),
                                                               type=LocationType.FROZEN_CHEST,
                                                               required_items_events=["Holy Eagle"]),
        "Kamui - Freestanding Chest in bear cave middle pillar": LocData(container_check_id(MapIds.KAMUI, 14),
                                                                         required_items_events=["Holy Eagle"]),
        "Kamui - Freestanding chest on ice cascade upper": LocData(container_check_id(MapIds.KAMUI, 13)),
    },

    RegionNames.KAMUI:
        {
            "Kamui - Buried Chest near Dojo": LocData(container_check_id(MapIds.KAMUI, 6),
                                                      type=LocationType.BURIED_CHEST),
            "Kamui - Frozen Chest near Dojo": LocData(container_check_id(MapIds.KAMUI, 16),
                                                      type=LocationType.FROZEN_CHEST),
            "Kamui - Frozen Chest near Yoichi's hut": LocData(container_check_id(MapIds.KAMUI, 19),
                                                              type=LocationType.FROZEN_CHEST),
            "Kamui - Buried Chest near Kokari's Fishing spot": LocData(container_check_id(MapIds.KAMUI, 22),
                                                                       type=LocationType.BURIED_CHEST),
        }
}

shop_locations = {
    RegionNames.KAMUI: {
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
warps={
    RegionNames.KAMUI_NORTHERN:[
        WarpData(WarpType.MERMAID_SPRING,Has("Kamui - Clear lake cursed torii"),Has("Kamui - Clear lake cursed torii"))
    ]
}