from typing import TYPE_CHECKING

from ..CheckIds import container_check_id
from ..Types import LocData, ExitData
from ..Enums.RegionNames import RegionNames, MapIds

if TYPE_CHECKING:
   from .. import OkamiWorld

exits = {

    RegionNames.FAWNS_HOUSE:[
        # Sends to pre Waka since we might not have beaten him yet
        ExitData(RegionNames.AGATA_FOREST_WAKA,required_items_events=["Agata Forest - Restore Guardian Sapling"],one_way=True)
    ]
}
events = {
}
locations = {
    RegionNames.FAWNS_HOUSE: {
        "Agata Forest - Stray Bead in Madame Fawn's": LocData(container_check_id(MapIds.AGATA_FOREST_MME_FAWN, 0))
    }
}
