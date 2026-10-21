from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from rule_builder.rules import True_, Has, HasAny, And, HasAll, Or
from ..CheckIds import container_check_id, shop_check_id, brush_check_id
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames, MapIds
from ..Enums.WarpType import WarpType
from ..Rules import long_swim_rule, slowdown_rule, has_portable_fire_source
from ..Types import ExitData, EventData, WarpData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.WAWKU_SHRINE_1F_CANONS: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_LOBBY, loading_screen=False,
                 required_items_events=["Wawku Shrine - 1F Defeat canons"])
    ],
    RegionNames.WAWKU_SHRINE_1F_LOBBY: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_SCALES, loading_screen=False,
                 required_items_events=["Wawku Shrine - 1F Melt ice block to west area"]),
        ExitData(RegionNames.WAWKU_SHRINE_1F_TOWER, loading_screen=False,
                 required_items_events=["Wawku Shrine - 1F Open Tower"])
    ],
    RegionNames.WAWKU_SHRINE_1F_TOWER: [
        ExitData(RegionNames.WAWKU_SHRINE_2F_TOWER, loading_screen=False, one_way=True)
    ],
    RegionNames.WAWKU_SHRINE_2F_TOWER: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_TOWER, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LOBBY, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_3F_TOWER, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LEDGE, loading_screen=False, one_way=True),
    ],
    RegionNames.WAWKU_SHRINE_3F_TOWER: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_TOWER, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LOBBY, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_2F_TOWER, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_2F_TOWER_BOMB, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_4F_TOWER, loading_screen=False, special_rule=slowdown_rule),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LEDGE, loading_screen=False, one_way=True),
    ],
    RegionNames.WAWKU_SHRINE_2F_TOWER_BOMB: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_TOWER, loading_screen=False, one_way=True,
                 required_items_events=["Wawku Shrine - 2F Blow wall in tower"]),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LOBBY, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LEDGE, loading_screen=False, one_way=True),
    ],
    RegionNames.WAWKU_SHRINE_4F_TOWER: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_TOWER, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LOBBY, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_2F_TOWER, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_1F_LEDGE, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_4F_OUTSIDE, loading_screen=False, special_rule=slowdown_rule),
        ExitData(RegionNames.WAWKU_SHRINE_5F_TOWER, loading_screen=False, one_way=True,
                 special_rule=HasAny(BrushTechniques.BLIZZARD, BrushTechniques.ICESTORM)),
    ],
    RegionNames.WAWKU_SHRINE_1F_LEDGE: [
        ExitData(RegionNames.WAWKU_SHRINE_1F_LOBBY, loading_screen=False, one_way=True),
    ],
    RegionNames.WAWKU_SHRINE_4F_OUTSIDE: [
        ExitData(RegionNames.WAWKU_SHRINE_4F_GATCHA, loading_screen=False, one_way=True),
        ExitData(RegionNames.WAWKU_SHRINE_4F_CLOCKWORK, loading_screen=False,
                 required_items_events=["Wawku Shrine - 4F open Clockwork door"]),
    ],
    RegionNames.WAWKU_SHRINE_4F_GATCHA: [
        ExitData(RegionNames.WAWKU_SHRINE_4F_OUTSIDE, loading_screen=False, one_way=True,
                 special_rule=HasAny(BrushTechniques.BLIZZARD, BrushTechniques.ICESTORM))
    ],
    RegionNames.WAWKU_SHRINE_4F_LEDGE: [
        ExitData(RegionNames.WAWKU_SHRINE_4F_TOWER, one_way=True, loading_screen=False)
    ],
    RegionNames.WAWKU_SHRINE_5F_TOWER: [
        ExitData(RegionNames.WAWKU_SHRINE_4F_LEDGE, one_way=True, loading_screen=False),
        ExitData(RegionNames.WAWKU_SHRINE_5F_TOWER_OUTER, one_way=True, loading_screen=False,
                 special_rule=And(HasAny(BrushTechniques.INFERNO, BrushTechniques.FIREBURST),
                                  Has(BrushTechniques.GREENSPROUT_VINE)))
    ],
    RegionNames.WAWKU_SHRINE_5F_TOWER_OUTER: [
        ExitData(RegionNames.WAWKU_SHRINE_6F, one_way=True, loading_screen=False,
                 special_rule=And(HasAny(BrushTechniques.BLIZZARD, BrushTechniques.ICESTORM),
                                  Has(BrushTechniques.CATWALK)))
    ],
    RegionNames.WAWKU_SHRINE_6F: [
        ExitData(RegionNames.WAWKU_SHRINE_6F_OUTSIDE,
                 special_rule=And(Has(BrushTechniques.BLIZZARD), has_portable_fire_source,
                                  Has(BrushTechniques.POWER_SLASH))),
        ExitData(RegionNames.WAWKU_SHRINE_5F_TOWER_OUTER, one_way=True, loading_screen=False)
    ],
    RegionNames.WAWKU_SHRINE_6F_OUTSIDE: [
        ExitData(RegionNames.WAWKU_SHRINE_6F_NECHKU,
                 special_rule=Or(slowdown_rule, HasAny(BrushTechniques.GALESTORM, BrushTechniques.WHIRLWIND),
                                 Has(BrushTechniques.POWER_SLASH)))
    ],
    RegionNames.WAWKU_SHRINE_4F_CLOCKWORK: [
        ExitData(RegionNames.WAWKU_SHRINE_4F_CLOCKWORK_AFTER_GAP,
                 special_rule=And(slowdown_rule, HasAll(BrushTechniques.BLIZZARD, BrushTechniques.POWER_SLASH)))
    ],
    RegionNames.WAWKU_SHRINE_4F_CLOCKWORK_AFTER_GAP: [
        ExitData(RegionNames.WAWKU_SHRINE_4F_LECHKU_ARENA, required_items_events=["Wawku Shrine - 4F get Key"],
                 loading_screen=False)
    ]
}
events = {
    RegionNames.WAWKU_SHRINE_1F_CANONS: {
        "Wawku Shrine - 1F Defeat canons": EventData(special_rule=slowdown_rule, power_slash_level=1)
    },
    RegionNames.WAWKU_SHRINE_1F_LOBBY: {
        "Wawku Shrine - 1F Melt ice block to west area": EventData(
            special_rule=HasAny(BrushTechniques.INFERNO, BrushTechniques.FIREBURST)),
        "Wawku Shrine - 1F Open Tower": EventData(required_items_events=["Wawku Shrine - 1F get Key"])
    },
    RegionNames.WAWKU_SHRINE_1F_SCALES: {
        "Wawku Shrine - 1F balance Scale": EventData(
            special_rule=And(HasAny(BrushTechniques.INFERNO, BrushTechniques.FIREBURST),
                             HasAll(BrushTechniques.GREENSPROUT_BLOOM, "Holy Eagle"))),
        "Wawku Shrine - 1F get Key": EventData(required_brush_techniques=[BrushTechniques.GALESTORM],
                                               required_items_events=["Wawku Shrine - 1F balance Scale"])
    },
    RegionNames.WAWKU_SHRINE_1F_TOWER: {
        "Wawku Shrine - 1F Climb Tower with waterspout pillar": EventData(
            special_rule=And(HasAny(BrushTechniques.INFERNO, BrushTechniques.FIREBURST),
                             Has(BrushTechniques.WATERSPOUT)))
    },
    RegionNames.WAWKU_SHRINE_2F_TOWER_BOMB: {
        "Wawku Shrine - 2F Blow wall in tower": EventData(cherry_bomb_level=1)
    },
    RegionNames.WAWKU_SHRINE_4F_TOWER: {
        "Wawku Shrine - 4F open Clockwork door": EventData(
            required_items_events=["Wawku Shrine - 6F Get Clockwork Key"])
    },
    RegionNames.WAWKU_SHRINE_4F_GATCHA: {
        "Wawku Shrine - 4F Mandatory Fight before gatcha machine": EventData(
            mandatory_enemies=[OkamiEnemies.GREAT_TENGU]),
        "Wawku Shrine - 4F Win the gatcha": EventData(
            special_rule=And(HasAny(BrushTechniques.INFERNO, BrushTechniques.FIREBURST),
                             HasAll("Wawku Shrine - 4F Mandatory Fight before gatcha machine",
                                    BrushTechniques.POWER_SLASH)))
    },
    RegionNames.WAWKU_SHRINE_6F_NECHKU: {
        "Wawku Shrine - 6F Defeat Nechku": EventData(
            mandatory_enemies=[OkamiEnemies.NECHKU]),
        "Wawku Shrine - 6F Get Clockwork Key": EventData(required_items_events=["Wawku Shrine - 6F Defeat Nechku"]),
    },
    RegionNames.WAWKU_SHRINE_4F_CLOCKWORK: {
        "Wawku Shrine - 4F Destroy cannons": EventData(required_brush_techniques=[BrushTechniques.INFERNO])
    },
    RegionNames.WAWKU_SHRINE_4F_CLOCKWORK_AFTER_GAP: {
        "Wawku Shrine - 4F clear Fire spinner room": EventData(
            special_rule=And(HasAny(BrushTechniques.BLIZZARD, BrushTechniques.ICESTORM),
                             HasAny(BrushTechniques.INFERNO, BrushTechniques.FIREBURST),
                             Has(BrushTechniques.GALESTORM))),
        "Wawku Shrine - 4F get Key": EventData(cherry_bomb_level=1,
                                               required_items_events=["Wawku Shrine - 4F clear Fire spinner room"])
    },
    RegionNames.WAWKU_SHRINE_4F_LECHKU_ARENA: {
        "Wawku Shrine - Defeat Leckhu and Nechku": EventData(
            mandatory_enemies=[OkamiEnemies.NECHKU, OkamiEnemies.LECHKU])
    }
}
locations = {
    RegionNames.WAWKU_SHRINE_1F_CANONS: {
        "Wawku Shrine - 1F Left Buried chest under canon": LocData(container_check_id(MapIds.WAWKU_SHRINE, 0),
                                                                   required_items_events=[
                                                                       "Wawku Shrine - 1F Defeat canons"]),
        "Wawku Shrine - 1F Right Buried chest under canon": LocData(container_check_id(MapIds.WAWKU_SHRINE, 1),
                                                                    required_items_events=[
                                                                        "Wawku Shrine - 1F Defeat canons"])
    },
    RegionNames.WAWKU_SHRINE_1F_SCALES: {
        "Wawku Shrine - 1F Freestanding chest in scales room": LocData(container_check_id(MapIds.WAWKU_SHRINE, 14),
                                                                       required_items_events=["Holy Eagle"])
    },
    RegionNames.WAWKU_SHRINE_1F_LEDGE: {
        "Wawku Shrine - 1F Freestanding Chest on tower ledge west": LocData(container_check_id(MapIds.WAWKU_SHRINE, 3))
    },
    RegionNames.WAWKU_SHRINE_2F_TOWER_BOMB: {
        "Wawku Shrine - 2F Freestanding chest in tower near bombable wall": LocData(
            container_check_id(MapIds.WAWKU_SHRINE, 2))
    },
    RegionNames.WAWKU_SHRINE_4F_OUTSIDE: {
        "Wawku Shrine - 4F Freestanding chest on platform over east spinners": LocData(
            container_check_id(MapIds.WAWKU_SHRINE, 5), required_items_events=["Holy Eagle"]),
        "Wawku Shrine - 4F Frozen chest outside": LocData(container_check_id(MapIds.WAWKU_SHRINE, 6),
                                                          type=LocationType.FROZEN_CHEST),
        "Wawku Shrine - 4F Freestanding chest on ledge outside near fire spider": LocData(
            container_check_id(MapIds.WAWKU_SHRINE, 7),
            special_rule=HasAny(BrushTechniques.BLIZZARD, BrushTechniques.ICESTORM))
    },
    RegionNames.WAWKU_SHRINE_4F_GATCHA: {
        "Wawku Shrine - Itegami": LocData(brush_check_id(23),
                                          required_items_events=["Wawku Shrine - 4F Win the gatcha"]),
        "Wawku Shrine - Itegami (Icestorm)": LocData(brush_check_id(24),
                                                     required_items_events=["Wawku Shrine - 4F Win the gatcha"])
    },
    RegionNames.WAWKU_SHRINE_4F_LEDGE: {
        "Wawku Shrine - 4F Freestanding chest on tower ledge": LocData(container_check_id(MapIds.WAWKU_SHRINE, 4))
    },
    RegionNames.WAWKU_SHRINE_5F_TOWER: {
        "Wawku Shrine - 5F Freestanding chest on tower lone ledge": LocData(container_check_id(MapIds.WAWKU_SHRINE, 8),
                                                                            special_rule=HasAny(
                                                                                BrushTechniques.BLIZZARD,
                                                                                BrushTechniques.ICESTORM))
    },
    RegionNames.WAWKU_SHRINE_6F: {
        "Wawku Shrine - 6F Frozen chest in spinners room": LocData(container_check_id(MapIds.WAWKU_SHRINE, 9),
                                                                   type=LocationType.FROZEN_CHEST,
                                                                   special_rule=Or(slowdown_rule,
                                                                                   Has(BrushTechniques.BLIZZARD)))
    },
    RegionNames.WAWKU_SHRINE_6F_NECHKU: {
        "Wawku Shrine - 6F Left Frozen chest before Nechku": LocData(container_check_id(MapIds.WAWKU_SHRINE, 11),
                                                                     type=LocationType.FROZEN_CHEST),
        "Wawku Shrine - 6F Right Frozen chest before Nechku": LocData(container_check_id(MapIds.WAWKU_SHRINE, 10),
                                                                      type=LocationType.FROZEN_CHEST)
    },
    RegionNames.WAWKU_SHRINE_4F_CLOCKWORK_AFTER_GAP: {
        "Wawku Shrine - 4F Burning chest in Flaming spinners room": LocData(container_check_id(MapIds.WAWKU_SHRINE, 18),
                                                                            type=LocationType.BURNING_CHEST,
                                                                            required_items_events=[
                                                                                "Wawku Shrine - 4F clear Fire spinner room"])
    },
    RegionNames.WAWKU_SHRINE_4F_LECHKU_ARENA: {
        "Wawku Shrine - 4F Left Frozen chest before Lechku": LocData(container_check_id(MapIds.WAWKU_SHRINE, 12),
                                                                     type=LocationType.FROZEN_CHEST),
        "Wawku Shrine - 4F Right Frozen chest before Lechku": LocData(container_check_id(MapIds.WAWKU_SHRINE, 13),
                                                                      type=LocationType.FROZEN_CHEST),
        "Wawku Shrine - Lechku and Nechku reward": LocData(1300, required_items_events=[
            "Wawku Shrine - Defeat Leckhu and Nechku"], progress_type=LocationProgressType.EXCLUDED)
    },

}

shop_locations = {
    RegionNames.WAWKU_SHRINE_4F_LECHKU_ARENA: {
        "Wawku Shrine - Shop Slot 1": LocData(shop_check_id(20, 0), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 2": LocData(shop_check_id(20, 1), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 3": LocData(shop_check_id(20, 2), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 4": LocData(shop_check_id(20, 3), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 5": LocData(shop_check_id(20, 4), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 6": LocData(shop_check_id(20, 5), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 7": LocData(shop_check_id(20, 6), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 8": LocData(shop_check_id(20, 7), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 9": LocData(shop_check_id(20, 8), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 10": LocData(shop_check_id(20, 9), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 11": LocData(shop_check_id(20, 10), type=LocationType.SHOP),
        "Wawku Shrine - Shop Slot 12": LocData(shop_check_id(20, 11), type=LocationType.SHOP),
    }
}
