from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits={
    RegionNames.CURSED_TAKA_PASS:[ExitData("To Taka pass cave",RegionNames.CURSED_TAKA_PASS_WAKA,has_events=["Taka Pass - Blow up boulder to cave"])],
    # Region for mandatory waka encounter
    RegionNames.CURSED_TAKA_PASS_WAKA: [ExitData("Defeat Waka Again",RegionNames.CURSED_TAKA_PASS_CAVE, has_events=["Taka Pass - Rematch with Waka"])],
    RegionNames.CURSED_TAKA_PASS_CAVE : [ExitData("Cross Bridge to Guardian Sapling",RegionNames.CURSED_TAKA_PASS_GUARDIAN_SAPLING,has_events=["Taka pass - Restore Bridge to Guardian Sapling"])],
    RegionNames.CURSED_TAKA_PASS_GUARDIAN_SAPLING: [ExitData("Taka Pass Restoraztion",RegionNames.TAKA_PASS,has_events=["Taka pass - Restore Guardian Sapling"])]
}
events={
    RegionNames.CURSED_TAKA_PASS:{
        "Taka Pass - Blow up boulder to cave" : EventData(cherry_bomb_level=1)
    },
    RegionNames.CURSED_TAKA_PASS_WAKA:{
        "Taka Pass - Rematch with Waka":EventData(mandatory_enemies=[OkamiEnnemies.WAKA_2])
    },
    RegionNames.CURSED_TAKA_PASS_CAVE:{
        "Taka pass - Restore Bridge to Guardian Sapling":EventData(required_brush_techniques=[BrushTechniques.REJUVENATION])
    },
    RegionNames.CURSED_TAKA_PASS_GUARDIAN_SAPLING: {
        "Taka pass - Restore Guardian Sapling": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM])
    },
}

locations = {
    RegionNames.CURSED_TAKA_PASS_CAVE:{
        "Taka pass - Stray bead chest in cave pond" : LocData(96, type=LocationType.UNDERWATER_CHEST),
        "Taka pass - Burning chest in cave upper": LocData(97, type=LocationType.BURNING_CHEST),
        "Taka pass - Second Burning chest in cave upper": LocData(98, type=LocationType.BURNING_CHEST_NO_WATER),
    }

}