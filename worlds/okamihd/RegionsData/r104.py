from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.TSUTA_RUINS_1F_MAIN_PART: [
        ExitData("Tsuta Ruins - Push the glass ball", RegionNames.TSUTA_RUINS_MUSHROOMS,
                 has_events=["Tsuta Ruins - Mandatory Single Ogre Fight"]
                 ),
        ExitData("Tsuta Ruins - Left side door", RegionNames.TSUTA_RUINS_LEFT_SIDE,
                 has_events=["Tsuta Ruins - Defeat Blockhead"]),
        ExitData("Tsuta Ruins - Enter Inner Statue", RegionNames.TSUTA_RUINS_CENTRAL_STATUE,
                 has_events=["Tsuta Ruins - Destroy Poison Pots"])
    ],
    RegionNames.TSUTA_RUINS_MUSHROOMS: [
        ExitData("Tsuta Ruins - Cross flimsy bridge to left side", RegionNames.TSUTA_RUINS_LEFT_SIDE,
                 has_events=["Tsuta Ruins - Blow up weakened wall above Mushrooms"])
    ],
    RegionNames.TSUTA_RUINS_LEFT_SIDE: [
        ExitData("Tsuta Ruins - Cross the repaired Bridge", RegionNames.TSUTA_RUINS_DEVIL_GATES,
                 has_events=["Tsuta Ruins - Restore Bridge to Devil Gates' room"])
    ],
    RegionNames.TSUTA_RUINS_CENTRAL_STATUE: [
        ExitData("Tsuta Ruins - Enter the spider queen's lair", RegionNames.TSUTA_RUINS_SPIDER,
                 has_events=["Tsuta Ruins - Open the top of the statue"])
    ]
}
events = {
    RegionNames.TSUTA_RUINS_1F_MAIN_PART: {
        "Tsuta Ruins - Mandatory Single Ogre Fight": EventData(mandatory_enemies=[OkamiEnnemies.BUD_OGRE])
    },
    RegionNames.TSUTA_RUINS_MUSHROOMS: {
        "Tsuta Ruins - Mandatory Double Ogre Fight": EventData(mandatory_enemies=[OkamiEnnemies.BUD_OGRE]),
        "Tsuta Ruins - Grow the Mushrooms": EventData(required_brush_techniques=[BrushTechniques.SUNRISE],
                                                      required_items_events=[
                                                          "Tsuta Ruins - Mandatory Double Ogre Fight"]),
        "Tsuta Ruins - Blow up weakened wall above Mushrooms": EventData(cherry_bomb_level=1, required_items_events=[
            "Tsuta Ruins - Grow the Mushrooms"])
    },
    RegionNames.TSUTA_RUINS_LEFT_SIDE: {
        # Maybe add a check that Celestial Brush is unlocked to do this, i'm not sure this matters a lot
        "Tsuta Ruins - Defeat Blockhead": EventData(),
        "Tsuta Ruins - Open Lockjaw with Exorcising Arrow": EventData(
            required_items_events=["Tsuta Ruins - Defeat Blockhead"]),
        "Tsuta Ruins - Restore Bridge to Devil Gates' room": EventData(
            required_items_events=["Tsuta Ruins - Open Lockjaw with Exorcising Arrow"],
            required_brush_techniques=[BrushTechniques.REJUVENATION])
    },
    RegionNames.TSUTA_RUINS_DEVIL_GATES: {
        "Tsuta Ruins - Defeat Devil Gate 1": EventData(
            mandatory_enemies=[OkamiEnnemies.GREEN_IMP, OkamiEnnemies.DEAD_FISH]),
        "Tsuta Ruins - Defeat Devil Gate 2": EventData(
            mandatory_enemies=[OkamiEnnemies.GREEN_IMP, OkamiEnnemies.YELLOW_IMP]),
        "Tsuta Ruins - Defeat Devil Gate 3": EventData(
            mandatory_enemies=[OkamiEnnemies.RED_IMP, OkamiEnnemies.BUD_OGRE]),
        "Tsuta Ruins - Grow Mushrooms in Devil Gates Room": EventData(
            required_items_events=["Tsuta Ruins - Defeat Devil Gate 1", "Tsuta Ruins - Defeat Devil Gate 2",
                                   "Tsuta Ruins - Defeat Devil Gate 3"],
            required_brush_techniques=[BrushTechniques.SUNRISE]),
        "Tsuta Ruins - Destroy Poison Pots": EventData(
            required_items_events=["Tsuta Ruins - Grow Mushrooms in Devil Gates Room"])
    },
    RegionNames.TSUTA_RUINS_CENTRAL_STATUE: {
        "Tsuta Ruins - Bloom every cursed patch inside statue": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM]),
        "Tsuta Ruins - Open the top of the statue": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Tsuta Ruins - Defeat the spider queen": EventData(mandatory_enemies=[OkamiEnnemies.SPIDER_QUEEN])
    }
}
locations = {
    RegionNames.TSUTA_RUINS_1F_MAIN_PART: {
        "Tsuta Ruins - Freestanding Chest at Entrance": LocData(78),
        "Tsuta Ruins - Treasure Bud in Entrance Hall Middle": LocData(79, type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Treasure Bud in Entrance Hall Right Side": LocData(80, type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Chest in Entrance Hall near right side door": LocData(81),
        "Tsuta Ruins - Treasure Bud on 1F rightside path before ledge": LocData(82, type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Treasure Bud near glass ball": LocData(83, type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Stray bead chest on 1F rightside path upper part": LocData(96, required_brush_techniques=[
            BrushTechniques.GREENSPROUT_VINE])
    },
    RegionNames.TSUTA_RUINS_MUSHROOMS: {
        "Tsuta Ruins - Treasure bud behind logs in Mushrooms room": LocData(84, power_slash_level=1,
                                                                            type=LocationType.TREASURE_BUD)
    },
    RegionNames.TSUTA_RUINS_LEFT_SIDE: {
        "Tsuta Ruins - Treasure Bud behind hidden bombable wall on third plaform.": LocData(85, cherry_bomb_level=1,
                                                                                            type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Treasure Bud behind Lockjaw": LocData(86, type=LocationType.TREASURE_BUD, required_items_events=[
            "Tsuta Ruins - Open Lockjaw with Exorcising Arrow"]),
        "Tsuta Ruins - Left side hidden treasure bud": LocData(95, required_brush_techniques=[
            BrushTechniques.GREENSPROUT_VINE], type=LocationType.TREASURE_BUD)
    },
    RegionNames.TSUTA_RUINS_DEVIL_GATES: {
        "Tsuta Ruins - Treasure Bud near Devil gates": LocData(87,type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Treasure Bud #2 near Devil gates": LocData(88, type=LocationType.TREASURE_BUD),
        "Tsuta Ruins - Map Chest near poison pots": LocData(89, required_items_events=[
            "Tsuta Ruins - Grow Mushrooms in Devil Gates Room"]),
        "Tsuta Ruins - Treasure Bud behind waterfall bombable wall": LocData(90, required_items_events=[
            "Tsuta Ruins - Destroy Poison Pots"], cherry_bomb_level=1, type=LocationType.TREASURE_BUD)
    },
    RegionNames.TSUTA_RUINS_CENTRAL_STATUE: {
        "Tsuta Ruins - Tsutagami": LocData(91, required_items_events=[
            "Tsuta Ruins - Bloom every cursed patch inside statue"], type=LocationType.CONSTELLATION)
    },
    RegionNames.TSUTA_RUINS_SPIDER: {
        "Tsuta Ruins - Left Chest before Spider queen": LocData(92),
        "Tsuta Ruins - Right Chest before Spider queen": LocData(93),
        "Tsuta Ruins - Boss reward": LocData(94, required_items_events=["Tsuta Ruins - Defeat the spider queen"])
    }
}
