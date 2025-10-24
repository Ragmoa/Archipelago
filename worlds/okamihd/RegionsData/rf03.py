from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.CURSED_AGATA_FOREST: [ExitData("Agata Forest Restoration",RegionNames.AGATA_FOREST_WAKA),ExitData("Enter Madame Fawn's house",RegionNames.FAWNS_HOUSE)],
}
events = {
    RegionNames.CURSED_AGATA_FOREST: {
        "Agata Forest - Restore Guardian Sapling": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM],cherry_bomb_level=1, precollected=lambda o:o.BloomGuardianSaplings)
    },
}
locations = {
    RegionNames.CURSED_AGATA_FOREST:{
        "Agata Forest - Burning Chest near Madame Fawn's 1": LocData(0x0148000D,type=LocationType.BURNING_CHEST),
        "Agata Forest - Burning Chest near Madame Fawn's 2": LocData(0x0148000E,type=LocationType.BURNING_CHEST),
        "Agata Forest - Burning Chest near Madame Fawn's 3": LocData(0x0148000F,type=LocationType.BURNING_CHEST),
        "Agata Forest - Ledge chest near Madame Fawn's ": LocData(0x01480013, required_brush_techniques=[BrushTechniques.WATERSPOUT]),
    },
    RegionNames.FAWNS_HOUSE:{
        "Agata Forest - Stray Bead in Madame Fawn's":LocData(0x010B0000)
    }
}
