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
    RegionNames.INNER_YOSHPET_ENTRANCE: [
        ExitData(RegionNames.YOSHPET_MIDDLE, one_way=True),
        ExitData(RegionNames.INNER_YOSHPET_1_1),
    ],
    RegionNames.INNER_YOSHPET_1_1: [
        ExitData(RegionNames.INNER_YOSHPET_2_1),
    ],
    RegionNames.INNER_YOSHPET_2_1: [
        ExitData(RegionNames.INNER_YOSHPET_3_1),
        ExitData(RegionNames.INNER_YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.INNER_YOSHPET_3_1: [
        ExitData(RegionNames.INNER_YOSHPET_3_2, loading_screen=False, required_items_events=["Holy Eagle"]),
        ExitData(RegionNames.INNER_YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.INNER_YOSHPET_3_2: [
        ExitData(RegionNames.INNER_YOSHPET_3_3, loading_screen=False, required_items_events=["Holy Eagle"]),
        ExitData(RegionNames.INNER_YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.INNER_YOSHPET_3_3: [
        ExitData(RegionNames.INNER_YOSHPET_GATE, one_way=True),
        ExitData(RegionNames.INNER_YOSHPET_ENTRANCE, one_way=True)
    ],
    RegionNames.INNER_YOSHPET_GATE: [
        ExitData(RegionNames.INNER_YOSHPET_ENTRANCE, one_way=True)
    ]
}
events = {
    RegionNames.INNER_YOSHPET_GATE: {
        "Inner Yoshpet - Unlock Spirit Gate Warp point": EventData()
    }
}
locations = {
    RegionNames.INNER_YOSHPET_1_1: {
        "Inner Yoshpet - First Section - Freestanding chest after entrance vine wall": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 12)),
        # "Inner Yoshpet - First Section - Hourglass orb after first ice slope": LocData(
        #    container_check_id(MapIds.INNER_YOSHPET, 13), type=LocationType.HOURGLASS_ORB),
        "Inner Yoshpet - First Section - Freestanding chest after snow balls": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 0)),
        # "Inner Yoshpet - First Section - Hourglass orb on cliffs middle point after snow balls": LocData(
        #    container_check_id(MapIds.INNER_YOSHPET, 1), type=LocationType.HOURGLASS_ORB),
        "Inner Yoshpet - First Section - Freestanding chest at right end of final fork": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 2)),
    },
    RegionNames.INNER_YOSHPET_2_1: {
        # "Inner Yoshpet - Second Section - Hourglass orb on central stone after vine walls at entrance": LocData(
        #    container_check_id(MapIds.INNER_YOSHPET, 3), type=LocationType.HOURGLASS_ORB),
        "Inner Yoshpet - Second Section - Freestanding chest on cliff after vine walls at entrance": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 4)),
        # "Inner Yoshpet - Second Section - Hourglass orb after poison lake": LocData(
        #    container_check_id(MapIds.INNER_YOSHPET, 5), type=LocationType.HOURGLASS_ORB),
        "Inner Yoshpet - Second Section - Freestanding chest at left end of final fork": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 6)),
    },
    RegionNames.INNER_YOSHPET_3_1: {
        # "Inner Yoshpet - Third Section - Hourglass orb before catwalk section": LocData(
        #    container_check_id(MapIds.INNER_YOSHPET, 7), type=LocationType.HOURGLASS_ORB),
    },
    RegionNames.INNER_YOSHPET_3_2: {
        "Inner Yoshpet - Third Section - Freestanding chest in catwalk pit right": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 8)),
    },
    RegionNames.INNER_YOSHPET_3_3: {
        # "Inner Yoshpet - Third Section - Hourglass orb after catwalk section": LocData(
        #    container_check_id(MapIds.INNER_YOSHPET, 9), type=LocationType.HOURGLASS_ORB),
        "Inner Yoshpet - Third Section - Freestanding chest after catwalk pit and vine wall": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 10)),
        "Inner Yoshpet - Second Section - Buried chest at right end of final fork": LocData(
            container_check_id(MapIds.INNER_YOSHPET, 11)),
    }
}
warps = {
    RegionNames.INNER_YOSHPET_GATE: [
        WarpData(type=WarpType.MIST_WARP, trigger_warp_to=Has("Inner Yoshpet - Unlock Spirit Gate Warp point"),
                 trigger_warp_from=True_)
    ]
}
