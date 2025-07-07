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
    RegionNames.CURSED_TAKA_PASS_WAKA: ExitData("Defat Waka",RegionNames.CURSED_TAKA_PASS_CAVE, has_events=["Taka Pass - Rematch with Waka"]),
}
events={
    RegionNames.CURSED_TAKA_PASS:{
        "Taka Pass - Blow up boulder to cave" : EventData(cherry_bomb_level=1)
    },
    RegionNames.CURSED_TAKA_PASS_WAKA:{
        "Taka Pass - Rematch with Waka":EventData(mandatory_enemies=[OkamiEnnemies.WAKA_2])
    }
}

locations = {
    RegionNames.CURSED_TAKA_PASS_CAVE:{
        "Taka pass - Stray bead chest in cave pond" : LocData(96, type=LocationType.UNDERWATRER_CHEST),
        "Taka pass - Burning chest in cave upper": LocData(97, type=LocationType.BURNING_CHEST)
    }

}