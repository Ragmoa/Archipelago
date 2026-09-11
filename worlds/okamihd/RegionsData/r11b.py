from typing import TYPE_CHECKING

from ..CheckIds import container_check_id
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Types import LocData, EventData, ExitData
from ..Enums.RegionNames import RegionNames, MapIds

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
}
events = {
    RegionNames.KAMUI_BANDIT_SPIDER: {
        "Kamui - Defeat Bandit Spider in cave": EventData(
            mandatory_enemies=[OkamiEnemies.BANDIT_SPIDER]),
        # Headless Guardian, Bell Guardian
        "Kamui - Clear 10 Devil Gates in cave": EventData(
            mandatory_enemies=[OkamiEnemies.BLADE_NAMAHAGE, OkamiEnemies.UMBRELLA_NAMAHAGE, OkamiEnemies.IGLOO_TURTLE,
                               OkamiEnemies.BULL_CHARGER, OkamiEnemies.CLAY_DRUMMER, OkamiEnemies.CLAY_SAMURAI,
                               OkamiEnemies.CLAY_SHOGUN, OkamiEnemies.DOGU,OkamiEnemies.GREAT_TENGU,OkamiEnemies.WAKA_2, OkamiEnemies.EVIL_RAO, OkamiEnemies.NAGI],
            required_items_events=["Kamui - Defeat Bandit Spider in cave"]),
    }

}
locations = {
    RegionNames.KAMUI_BANDIT_SPIDER: {
        "Kamui - Chest after Bandit Spider": LocData(
            container_check_id(MapIds.KAMUI_BANDIT_SPIDER, 0),
            required_items_events=["Kamui - Defeat Bandit Spider in cave"]),
        "Kamui - Chest after 10 devil gates": LocData(
            container_check_id(MapIds.KAMUI_BANDIT_SPIDER, 1),
            required_items_events=["Kamui - Clear 10 Devil Gates in cave"])
    }
}
