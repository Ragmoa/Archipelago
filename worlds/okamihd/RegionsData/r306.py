from typing import TYPE_CHECKING

from rule_builder.rules import True_, Has, HasAny
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
    RegionNames.MOON_CAVE_100_OUTSIDE: [
        ExitData(RegionNames.MOON_CAVE_100,
                 required_items_events=["Moon Cave, 100 years ago - Mandatory Dogu fight at entrance"])
    ],
    RegionNames.MOON_CAVE_100: [
        ExitData(RegionNames.MOON_CAVE_100_OROCHI,loading_screen=False)
    ],

}
events = {
    RegionNames.MOON_CAVE_100_OUTSIDE: {
        "Moon Cave, 100 years ago - Mandatory Dogu fight at entrance": EventData(mandatory_enemies=[OkamiEnemies.DOGU])
    },
    RegionNames.MOON_CAVE_100: {
        "Moon Cave, 100 years ago - Collect 8 purification Sake": EventData()
    },
    RegionNames.MOON_CAVE_100_OROCHI: {
        "Moon Cave, 100 years ago - Defeat Orochi Again": EventData(mandatory_enemies=[OkamiEnemies.OROCHI_2]),
        "Moon Cave, 100 years ago - Defeat Orochi Cutscene": EventData(
            required_items_events=["Moon Cave, 100 years ago - Defeat Orochi Again"],
            required_brush_techniques=[BrushTechniques.CRESCENT], power_slash_level=1),
    }
}
locations = {

}
