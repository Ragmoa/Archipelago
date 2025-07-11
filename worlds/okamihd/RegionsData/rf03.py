from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
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
            required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM],cherry_bomb_level=1)
    },
}
locations = {
    RegionNames.CURSED_AGATA_FOREST:{
        "Agata Forest - Burning Chest near Madame Fawn's 1": LocData(58),
        "Agata Forest - Burning Chest near Madame Fawn's 2": LocData(59),
        "Agata Forest - Burning Chest near Madame Fawn's 3": LocData(60),
        "Agata Forest - Ledge chest near Madame Fawn's ": LocData(64, required_brush_techniques=[BrushTechniques.WATERSPROUT]),
    },
    RegionNames.FAWNS_HOUSE:{
        "Agata Forest - Stray Bead in Madame Fawn's":LocData(97)
    }
}
