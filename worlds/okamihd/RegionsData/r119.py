from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..CheckIds import container_check_id
from ..Enums.LocationType import LocationType
from ..Types import LocData, EventData
from ..Enums.RegionNames import RegionNames, MapIds

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
}
events = {
    RegionNames.KAMUI_BLOCKHEAD: {
        "Kamui - Defeat Blockhead Grande": EventData()
    }
}
locations = {
    RegionNames.KAMUI_BLOCKHEAD: {
        "Kamui - Left Chest in Blockhead Grande Cave": LocData(container_check_id(MapIds.BLOCKHEAD_GRANDE_CAVE, 0),
                                                               required_items_events=[
                                                                   "Kamui - Defeat Blockhead Grande"]),
        "Kamui - Center Chest in Blockhead Grande Cave": LocData(container_check_id(MapIds.BLOCKHEAD_GRANDE_CAVE, 1),
                                                                 required_items_events=[
                                                                     "Kamui - Defeat Blockhead Grande"]),
        "Kamui - Right Chest in Blockhead Grande Cave": LocData(container_check_id(MapIds.BLOCKHEAD_GRANDE_CAVE, 2),
                                                                required_items_events=[
                                                                    "Kamui - Defeat Blockhead Grande"])
    }

}
