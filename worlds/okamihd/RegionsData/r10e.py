from typing import TYPE_CHECKING

from ..Enums.LocationType import LocationType
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits={
    RegionNames.CALCIFIED_CAVERN:[ExitData("Moon Cave Entrance Bottom",RegionNames.MOON_CAVE,has_events=["Calcified Cavern - Fool Yokai Guards"])]
}
events={
    RegionNames.CALCIFIED_CAVERN:{
        #FIXME - Fill mandatory ennemies here
        "Calcified Cavern - Defeat devil gate" : EventData(mandatory_enemies=[]),
        "Calcified Cavern - Get Mask": EventData(required_items_events=["Calcified Cavern - Defeat devil gate"]),
        "Calcified Cavern - Fool Yokai Guards": EventData(required_items_events=["Calcified Cavern - Get Mask"])
    }
}
locations={
    RegionNames.CALCIFIED_CAVERN: {
        "Calcified Cavern - Freestanding item": LocData(171, type=LocationType.FREESTANDING_ITEM),
        #For now this is treated like a key, so not randomized.
        #"Calcified Cavern - Chest after devil gate": LocData(172, required_items_events=["Calcified Cavern - Defeat devil gate"]),
        "Calcified Cavern - Left Side chest":LocData(173),
        "Calcified Cavern - Frozen Chest": LocData(174,type=LocationType.FROZEN_CHEST)
    }
}