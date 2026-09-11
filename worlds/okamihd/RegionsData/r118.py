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
    RegionNames.KAMUI_EZOFUJI_PS3_CAVE: {
        "Kamui (Ezofuji) - Offer 360,000 yen in Power Slash 3 Fountain": EventData()
    }
}
locations = {
    RegionNames.NORTHERN_RYOSHIMA_COAST_CB2_CAVE: {
        # Brush upgrade id 12
        "Kamui (Ezofuji) - Tachigami (Power Slash 3)": LocData(13, type=LocationType.CONSTELLATION,
                                                               progress_type=LocationProgressType.EXCLUDED,
                                                               required_items_events=[
                                                                   "Kamui (Ezofuji) - Offer 360,000 yen in Power Slash 3 Fountain"]),
        "Kamui (Ezofuji) - Chest after Power Slash 3": LocData(container_check_id(MapIds.POWER_SLASH_3_CAVE, 0),
                                                               required_items_events=[
                                                                   "Kamui (Ezofuji) - Offer 360,000 yen in Power Slash 3 Fountain"])
    }

}
