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
    RegionNames.YOSHPET_ENTRANCE: [
        ExitData(RegionNames.KAMUI_NORTHERN, one_way=True),
        ExitData(RegionNames.YOSHPET_1_1)
    ],
    RegionNames.YOSHPET_1_1: [
        ExitData(RegionNames.YOSHPET_1_2, loading_screen=False,
                 required_items_events=["Yoshpet - First section - Pass high vine wall"]),
    ],
    RegionNames.YOSHPET_1_2: [
        ExitData(RegionNames.YOSHPET_2_1),
        # When running out of time
        ExitData(RegionNames.YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.YOSHPET_2_1: [
        ExitData(RegionNames.YOSHPET_3_1),
        # When running out of time
        ExitData(RegionNames.YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.YOSHPET_3_1: [
        ExitData(RegionNames.YOSHPET_MIDDLE, one_way=True),
        # When running out of time
        ExitData(RegionNames.YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.YOSHPET_MIDDLE: [
        #FIXME: Stub for Ponc'tan logic. Doesn't require anything.
        #ExitData(RegionNames.PONC_TAN)
        ExitData(RegionNames.YOSHPET_ENTRANCE, one_way=True)
    ]
}
events = {
    RegionNames.YOSHPET_1_1: {
        # Can be bypassed with a walljump.
        "Yoshpet - First section - Pass high vine wall": EventData(required_items_events=["Holy Eagle"])
    }
}
locations = {
    RegionNames.YOSHPET_1_1: {
        "Yoshpet - First section - Freestanding chest after vine wall at entrance": LocData(
            container_check_id(MapIds.YOSHPET, 16)),
        #"Yoshpet - First section - Hourglass orb after vine walls at cliff's bottom": LocData(
        #    container_check_id(MapIds.YOSHPET, 0), type=LocationType.HOURGLASS_ORB),
        "Yoshpet - First section - Freestanding chest near cliff's top": LocData(
            container_check_id(MapIds.YOSHPET, 12)),
       # "Yoshpet - First section - Hourglass orb on Frozen Lake Platforms": LocData(
       #     container_check_id(MapIds.YOSHPET, 13), type=LocationType.HOURGLASS_ORB),
        "Yoshpet - First section - Freestanding chest on Frozen Lake Platforms": LocData(
            container_check_id(MapIds.YOSHPET, 1)),

    },
    RegionNames.YOSHPET_1_2: {
        "Yoshpet - First section - Freestanding chest at left end of final fork": LocData(
            container_check_id(MapIds.YOSHPET, 2)),
    },
    RegionNames.YOSHPET_2_1: {
        "Yoshpet - Second section - Freestanding Chest after entrance": LocData(container_check_id(MapIds.YOSHPET, 3)),
        #"Yoshpet - Second section - Hourglass orb before first vine wall": LocData(
        #    container_check_id(MapIds.YOSHPET, 4), type=LocationType.HOURGLASS_ORB),
        "Yoshpet - Second section - Freestanding Chest between second and third vine wall": LocData(
            container_check_id(MapIds.YOSHPET, 5)),
        "Yoshpet - Second section - Freestanding Chest on ice platform in poison lake": LocData(
            container_check_id(MapIds.YOSHPET, 17)),
       # "Yoshpet - Second section -  Hourglass orb on ice platform in poison lake": LocData(
       #     container_check_id(MapIds.YOSHPET, 6), type=LocationType.HOURGLASS_ORB),
        "Yoshpet - Second section -  Freestanding chest before final fork": LocData(
            container_check_id(MapIds.YOSHPET, 7)),
        "Yoshpet - Second section - Freestanding chest at right end of final fork": LocData(
            container_check_id(MapIds.YOSHPET, 8)),
    },
    RegionNames.YOSHPET_3_1: {
        #"Yoshpet - Third section - Hourglass orb on ice lake after snow balls": LocData(
        #    container_check_id(MapIds.YOSHPET, 14), type=LocationType.HOURGLASS_ORB),
        "Yoshpet - Third section - Freestanding chest on ice lake after snow balls": LocData(
            container_check_id(MapIds.YOSHPET, 15)),
       #"Yoshpet - Third section - Hourglass orb after ice lake": LocData(
       #    container_check_id(MapIds.YOSHPET, 9), type=LocationType.HOURGLASS_ORB),
        "Yoshpet - Third section - Freestanding chest on hill's right side, after ice lake": LocData(
            container_check_id(MapIds.YOSHPET, 10)),
        # Not marking this one as buried since you can't use Crescent in Yoshpet. So this chest should never require it logically
        "Yoshpet - Third section - Buried chest at right end of final fork": LocData(
            container_check_id(MapIds.YOSHPET, 11)),
    }
}
