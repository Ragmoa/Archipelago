from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..CheckIds import container_check_id
from ..Enums.LocationType import LocationType
from ..Types import LocData, EventData, ExitData
from ..Enums.RegionNames import RegionNames, MapIds

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.KAMUI_CB3_CAVE: [
        ExitData(RegionNames.KAMUI_NORTHERN, one_way=True)
    ]
}
events = {
    RegionNames.KAMUI_CB3_CAVE: {
        "Kamui - Offer 300,000 yen in Cherry Bomb 3 Fountain": EventData()
    }
}
locations = {
    RegionNames.KAMUI_CB3_CAVE: {
        # Brush upgrade id 25
        "Kamui - Bakugami (Cherry Bomb 3)": LocData(26, type=LocationType.CONSTELLATION,
                                                    progress_type=LocationProgressType.EXCLUDED,
                                                    required_items_events=[
                                                        "Kamui - Offer 300,000 yen in Cherry Bomb 3 Fountain"]),
        "Kamui - Chest after Cherry Bomb 3": LocData(container_check_id(MapIds.CHERRY_BOMB_3_CAVE, 0),
                                                     required_items_events=[
                                                         "Kamui - Offer 300,000 yen in Cherry Bomb 3 Fountain"])
    }

}
