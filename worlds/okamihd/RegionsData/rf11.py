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


warps = {
    RegionNames.CURSED_KAMUI_PRE_FIGHT: [
        WarpData(WarpType.MIST_WARP, True_, Has("Kamui - Unlock mist warp point"))
    ]
}
