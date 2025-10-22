from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Rules import night_check_rule
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.SHINSHU_FIELD: [
        ExitData("Cross Cave to Agata Forest", RegionNames.SHINSHU_FIELD_AGATA_CAVE, needs_swim=True),
        ExitData("Enter Tama's house", RegionNames.TAMA_HOUSE),
        ExitData("To Moon Cave Entrance",RegionNames.MOON_CAVE_OUTSIDE)],
    RegionNames.SHINSHU_FIELD_AGATA_CAVE: [ExitData('To Cursed Agata Forest', RegionNames.CURSED_AGATA_FOREST,
                                                    has_events=["Shinshu Field - Open Entrance to Agata Forest"])]
}
events = {
    RegionNames.SHINSHU_FIELD_AGATA_CAVE: {
        "Shinshu Field - Open Entrance to Agata Forest": EventData(cherry_bomb_level=1)
    }
}
locations = {
    RegionNames.SHINSHU_FIELD: {
        "Shinshu Field - Buried chest between bushes behind merchant": LocData(0x01470000, type=LocationType.BURIED_CHEST),
        "Shinshu Field - Freestanding chest behind Guardian Sapling": LocData(0x01470001),
        "Shinshu Field - Buried chest between bushes near Tama's house": LocData(0x01470002, type=LocationType.BURIED_CHEST),
        "Shinshu Field - Buried chest between bushes near Lake": LocData(0x01470003, type=LocationType.BURIED_CHEST),
        "Shinshu Field - Chest Under Bombable ground near Agata Forest entrance": LocData(0x01470004, cherry_bomb_level=1,
                                                                                 required_brush_techniques=[
                                                                                     BrushTechniques.GREENSPROUT_BLOOM]),
        "Shinshu Field - Buried chest between bushes near Dojo": LocData(0x01470005, type=LocationType.BURIED_CHEST),
        "Shinshu Field - Chest after devil gate": LocData(0x01470006, mandatory_enemies=[OkamiEnnemies.GREEN_IMP,
                                                                                 OkamiEnnemies.RED_IMP,
                                                                                 OkamiEnnemies.YELLOW_IMP]),
        "Shinshu Field - Buried chest between bushes on ledge near sapling": LocData(0x01470007, type=LocationType.BURIED_CHEST),
        "Shinshu Field - Buried chest between bushes behind Klins": LocData(0x01470008, type=LocationType.BURIED_CHEST),
        # This is the cherry bomb tutorial. Need to check what happens if you blow the wall before doing the tutorial.
        "Shinshu Field - In Bombable cave near Tama's house": LocData(0x01470009, cherry_bomb_level=1),
        "Shinshu Field - In Bombable cave near cat statue": LocData(0x0147000A, cherry_bomb_level=1),
        "Shinshu Field - Buried Chest in leaf pile near Tama's house": LocData(0x0147000D,
                                                                               type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Shinshu Field - Chest on Big Torii": LocData(0x01470010, required_brush_techniques=[BrushTechniques.WATERSPOUT],
                                                      needs_swim=True),
        "Shinshu Field - Freestanding chest after Rejuvenating Guardian Sapling": LocData(0x01470013),
        "Shinshu Field - Freestanding chest near Agata Forest Cave": LocData(0x01470014),
        "Shinshu Field - Freestanding chest near Tama's house": LocData(0x01470019),
        "Shinshu Field - Buried Chest in burning leaf pile behind Dojo": LocData(0x0147001A, type=LocationType.BURIED_UNDER_LEAF_PILE)
    },

    RegionNames.TAMA_HOUSE: {

        "Shinshu Field - Bakigami": LocData(17, required_items_events=["Kamiki Village - Restore Sakuya's Tree"],type=LocationType.CONSTELLATION,
                                            special_rule=lambda s,w:night_check_rule(s,w))
    }
}
