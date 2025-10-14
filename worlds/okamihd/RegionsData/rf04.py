from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    # small region to force waka fight to be cleared before acessing the rest of the forest.
    RegionNames.AGATA_FOREST_WAKA: [
        ExitData("Agata Forest Waka cutscene", RegionNames.AGATA_FOREST, has_events=["Agata Forest - Defeat Waka"])],
    RegionNames.AGATA_FOREST: [ExitData("Agata Forest - To Taka Pass", RegionNames.CURSED_TAKA_PASS,
                                        has_events=["Agata Forest - Repair Bridge with Kokari"])
        , ExitData("Agata Ruins - Enter Tsuta Ruins", RegionNames.TSUTA_RUINS_1F_MAIN_PART,
                   has_events=["Agata Forest - Open Ruins Door"])]
}
events = {
    RegionNames.AGATA_FOREST_WAKA: {
        "Agata Forest - Defeat Waka": EventData(mandatory_enemies=[OkamiEnnemies.WAKA_1])
    },
    RegionNames.AGATA_FOREST: {
        "Agata Forest - Open Ruins Door": EventData(required_items_events=["Tsuta Ruins Key"]),
        # Probably might be changed to not reuquire beating Tsuta. Or to be open from the start.
        "Agata Forest - Repair Bridge with Kokari": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE],
            required_items_events=["Tsuta Ruins - Defeat the spider queen"]),
        "Agata Forest - Fill Kushi's Barrel": EventData(required_brush_techniques=[BrushTechniques.WATERSPOUT]),
        "Agata Forest - Fight with Susano": EventData(power_slash_level=1,
                                                      required_items_events=["Agata Forest - Fill Kushi's Barrel"]),
        "Agata Forest - Fish Whopper with Kokari": EventData(power_slash_level=1,
                                                             required_items_events=[
                                                                 "Agata Forest - Fight with Susano"]),
        "Agata Forest - Get Orb from Ume": EventData(id=127, mandatory_enemies=[OkamiEnnemies.UME],
                                                     is_event_item=lambda o: o.CanineRewards != 0,
                                                     progress_type=lambda
                                                         o: LocationProgressType.EXCLUDED if o.CanineRewards == 2 else LocationProgressType.DEFAULT,
                                                     event_item_name="Justice Orb",
                                                     required_items_events=["Agata Forest - Fish Whopper with Kokari"])
    }
}
locations = {
    RegionNames.AGATA_FOREST: {
        # the names here could be better.
        "Agata Forest - Treasure Bud near Guardian Sapling Cave": LocData(46, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud 1": LocData(47, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud on big island": LocData(48, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud island near Kokari": LocData(49, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud near Karude's house": LocData(50, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud near Karude's house cursed patch": LocData(51, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud near waterfall": LocData(52, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud near Mme. Fawn's Cave": LocData(53, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud 2": LocData(54, type=LocationType.TREASURE_BUD),
        "Agata Forest - Treasure Bud Inside Tree": LocData(55, type=LocationType.TREASURE_BUD),
        "Agata Forest - Chest at Guardian Sapling": LocData(56),
        "Agata Forest - Buried chest near shortcut": LocData(57, type=LocationType.BURIED_CHEST),
        # Probably needs something more to get on top
        "Agata Forest - Chest on top of the big tree": LocData(61, type=LocationType.UNDERWATER_CHEST,
                                                               required_brush_techniques=[
                                                                   BrushTechniques.GREENSPROUT_VINE]),
        "Agata Forest - Freestanding stray Bead": LocData(62,
                                                          required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE],
                                                          type=LocationType.FREESTANDING_ITEM),
        "Agata Forest - Freestanding Bull Horn": LocData(63,
                                                         required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE],
                                                         type=LocationType.FREESTANDING_ITEM),
        "Agata Forest - Buried Chest on Lake shore": LocData(65, type=LocationType.BURIED_CHEST),
        "Agata Forest - Buried Chest behind Karude's house": LocData(66, type=LocationType.BURIED_CHEST),
        "Agata Forest - Buried Chest on Island": LocData(67, type=LocationType.BURIED_CHEST),
        "Agata Forest - Chest under leaf pile near Shinshu Field entrance": LocData(68,
                                                                                    type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Agata Forest - Chest under leaf pile on ledge": LocData(69, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Agata Forest - Chest under leaf pile near river": LocData(70, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Agata Forest - Buried chest near Tsuta Ruins entrance": LocData(71, type=LocationType.STONE_BURIED_CHEST),
        # Add required event after Bridge cutscene
        "Agata Forest - Chest after Bridge cutscene": LocData(72),
        "Agata Forest - Chest near Demon Fang merchant": LocData(73),
        "Agata Forest - Chest near Tusta ruins door": LocData(74),
        "Agata Forest - Fish Giant Salmon with Kokari": LocData(77, power_slash_level=1),
        "Agata Forest - Yumigami": LocData(152, type=LocationType.CONSTELLATION,
                                           required_items_events=["Agata Forest - Fish Whopper with Kokari"])
    }
}
