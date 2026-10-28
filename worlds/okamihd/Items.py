import logging

from pygments.lexer import default

from BaseClasses import Item, ItemClassification
from .Enums.RegionNames import RegionNames
from .Types import OkamiItem, ItemData, LocalItem
from .Enums.BrushTechniques import BrushTechniques
from .Enums.DivineInstruments import DivineInstruments
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import OkamiWorld


def create_item(name: str, code: int, classification: ItemClassification, world: "OkamiWorld") -> Item:
    return OkamiItem(name, classification, code, world.player)


def create_standard_item(world: "OkamiWorld", name: str) -> Item:
    data = item_table[name]
    return create_item(name, data.code, data.classification, world)


def create_multiple_items(world: "OkamiWorld", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []
    for i in range(count):
        itemlist += [create_item(name, data.code, item_type, world)]

    return itemlist


def create_junk_items(world: "OkamiWorld", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    ic: ItemClassification

    junk_weights = build_junk_weights_pool(world)

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            # Weight 1 by default for unknown items, rework this for dynamic_junk_pool
            junk_list[name] = junk_weights.get(name, 1)

    for i in range(count):
        item = world.create_item(world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0])
        junk_pool.append(item)
    return junk_pool


def build_junk_weights_pool(world: "OkamiWorld") -> Dict[str, int]:
    weights = {}
    for group_name, group_data in get_item_name_groups().items():
        if group_name.startswith("filler"):
            match group_name:
                case "filler_battle":
                    weight = world.options.FillerBattleItemsRate.value
                case "filler_health_ink":
                    weight = world.options.FillerHealthInkItemsRate.value
                case "filler_feedbags":
                    weight = world.options.FillerFeedBagsRate.value
                case "filler_treasure_cheap":
                    weight = world.options.FillerCheapTreasuresRate.value
                case "filler_treasure_medium":
                    weight = world.options.FillerMediumTreasuresRate.value
                case "filler_treasure_expensive":
                    weight = world.options.FillerExpensiveTreasuresRate.value
                case "filler_fishes":
                    weight = world.options.FillerFishesRate.value
                case "filler_food":
                    weight = world.options.FillerFoodRate.value
                # Weight 0 for unknown filler groups
                case _:
                    weight = 0

            for item_name in group_data:
                weights[item_name] = weight

    return weights


def get_item_name_to_id_dict() -> dict:
    item_dict = {name: data.code for name, data in item_table.items()}
    return item_dict


def get_item_name_groups() -> dict:
    group_dict = {}
    for item_name, item_data in item_table.items():
        if item_data.item_groups is not None:
            for group_name in item_data.item_groups:
                if group_name in group_dict.keys():
                    entry = group_dict.get(group_name)
                    entry.append(item_name)
                    group_dict.update({group_name: entry})
                else:
                    group_dict[group_name] = [item_name]

    return group_dict


brush_techniques_items = {
    # Brush Techniques — item codes = 0x100 + game bitfield index (from BrushOverlay enum)
    BrushTechniques.GREENSPROUT_BLOOM.value: ItemData(0x104, ItemClassification.progression),  # bit 4
    BrushTechniques.GREENSPROUT_WATERLILY.value: ItemData(0x105, ItemClassification.progression),  # bit 5
    BrushTechniques.GALESTORM.value: ItemData(0x106, ItemClassification.progression),  # bit 6
    BrushTechniques.THUNDERSTORM.value: ItemData(0x108, ItemClassification.progression),  # bit 8
    BrushTechniques.INFERNO.value: ItemData(0x10A, ItemClassification.progression),  # bit 10
    BrushTechniques.POWER_SLASH.value: ItemData(0x10C, ItemClassification.progression, count_in_pool=3),  # bit 12
    BrushTechniques.WATERSPOUT.value: ItemData(0x10D, ItemClassification.progression),  # bit 13
    BrushTechniques.VEIL_OF_MIST.value: ItemData(0x110, ItemClassification.progression),  # bit 16
    BrushTechniques.CRESCENT.value: ItemData(0x112, ItemClassification.progression),  # bit 18
    BrushTechniques.GREENSPROUT_VINE.value: ItemData(0x113, ItemClassification.progression),  # bit 19
    # You always start with that one
    BrushTechniques.REJUVENATION.value: ItemData(0x116, ItemClassification.progression, count_in_pool=0),  # bit 22
    BrushTechniques.BLIZZARD.value: ItemData(0x117, ItemClassification.progression),  # bit 23
    BrushTechniques.CHERRY_BOMB.value: ItemData(0x119, ItemClassification.progression, count_in_pool=3),  # bit 25
    BrushTechniques.SUNRISE.value: ItemData(0x11B, ItemClassification.progression),  # bit 27
    BrushTechniques.CATWALK.value: ItemData(0x11E, ItemClassification.progression),  # bit 30
    ## UPGRADES/SECRET
    BrushTechniques.WHIRLWIND.value: ItemData(0x107, ItemClassification.progression),  # bit 7
    BrushTechniques.THUNDERBOLT.value: ItemData(0x109, ItemClassification.progression),  # bit 9
    BrushTechniques.FIREBURST.value: ItemData(0x10B, ItemClassification.progression),  # bit 11
    BrushTechniques.DELUGE.value: ItemData(0x10E, ItemClassification.progression),  # bit 14
    BrushTechniques.FOUNTAIN.value: ItemData(0x10F, ItemClassification.progression),  # bit 15
    BrushTechniques.MIST_WARP.value: ItemData(0x111, ItemClassification.progression),  # bit 17
    ## VERY SECRET ONE
    BrushTechniques.ICESTORM.value: ItemData(0x118, ItemClassification.progression),  # bit 24
}
equips = {
    # Equips
    "Water Tablet": ItemData(0x9c, ItemClassification.progression),
    "Peace Bell": ItemData(0x0b, ItemClassification.useful),
    "Golden Lucky Cat": ItemData(0x95, ItemClassification.useful),
    "Thief's Glove": ItemData(0x96, ItemClassification.useful),
    "Wood Mat": ItemData(0x97, ItemClassification.useful),
    # Has to be progression since we require it for some checks.
    "Golden Ink Pot": ItemData(0x98, ItemClassification.progression),
    "Fire Tablet": ItemData(0x9d, ItemClassification.progression)
}

quest_items = {
    # Quest Items
    "Canine Tracker": ItemData(0x42, ItemClassification.progression, count_in_pool=0),
    "Lucky Mallet": ItemData(0x43, ItemClassification.progression),
    "Border Key": ItemData(0x44, ItemClassification.progression, count_in_pool=0),
    "Dragon Orb": ItemData(0x45, ItemClassification.progression, count_in_pool=0),
    "Fox Rods": ItemData(0x46, ItemClassification.progression, count_in_pool=0),
    "Thunder Brew": ItemData(0x47, ItemClassification.progression),
    "Shell Amulet": ItemData(0x48, ItemClassification.progression, count_in_pool=0),

    "Mask": ItemData(0x49, ItemClassification.progression),
    "Golden Mushroom": ItemData(0x5f, ItemClassification.progression),
    "Gimmick Gear": ItemData(0x60, ItemClassification.progression),
    "8 Purification Sake": ItemData(0x62, ItemClassification.progression),
    "Sewaprolo": ItemData(0x63, ItemClassification.progression),
    "Charcoal": ItemData(0x71, ItemClassification.progression),
    "Blinding Snow": ItemData(0x72, ItemClassification.progression),
    "Treasure Box": ItemData(0x73, ItemClassification.progression, count_in_pool=0),
    "Herbal Medicine": ItemData(0x75, ItemClassification.progression),
    "Pinwheel": ItemData(0x76, ItemClassification.progression),
    "Marlin Rod": ItemData(0x77, ItemClassification.progression),
    # Not sure if this should be an item as we already have the power in the item pool...
    # "Fog Pot":ItemData(0x9f,ItemClassification.progression)
}
bitable_items = {
    ## "Biteable" Items
    ### As these disappear and respanw each time you transition, the best way to handle those would be to set the flag
    ### making them appear/respawn active, instead of giving them to the player
    ### at a potential place where they can't use them.
    ### Edit: So this Sake only resets if you go outside Kamiki village or on of its interiors;
    ### I'm not sure how that's going to work with ER.
    "Vista of the Gods": ItemData(0x5C, ItemClassification.progression),
    "Tsuta Ruins Key": ItemData(0x40, ItemClassification.progression),
    # "Oddly Shaped Turnip": ItemData(0x41, ItemClassification.progression)
}
useful_items = {
    # Useful items - Counts here are invalid, it's intended, to not fill the item pool with these
    "Sun Fragment": ItemData(0x05, ItemClassification.useful, count_in_pool=9),  # Should be 15
    "Astral Pouch": ItemData(0x06, ItemClassification.useful, count_in_pool=0),  # Intended
    "Stray Bead": ItemData(0xCC, ItemClassification.useful, count_in_pool=0),
    # Should be 99, set to 0 for now cause they mess with container collection states
    # probably will have to be changed to progession_skip balancing once DF shops get randomized
    "Demon Fang": ItemData(0x1F, ItemClassification.useful, count_in_pool=0),  # to see when DF shops get randomized
    # Technically a filler item, but useful feels more appropriate. Warping with those without Fountain will probably be out of logic.
    "Mermaid Coin": ItemData(0x0e, ItemClassification.useful, count_in_pool=5),
    # Accurate count, kept it since it isn't too much
    "Gold Dust": ItemData(0x9e, ItemClassification.useful, count_in_pool=11),
    # 15 if we count the ones sold by merchants, which we may randomize, only 1 in a chest if we don't count those...
    "Praise": ItemData(0x59, ItemClassification.useful, count_in_pool=0)  # Here for testing for now; Doesn't work
}

filler_items = {
    # Filler
    ## Battle Items 108, 23%
    "Exorcism Slip L": ItemData(0x08, ItemClassification.filler, item_groups=["filler_battle"]),
    "Exorcism Slip M": ItemData(0x09, ItemClassification.filler, item_groups=["filler_battle"]),
    "Exorcism Slip S": ItemData(0x0a, ItemClassification.filler, item_groups=["filler_battle"]),
    "Vengeance Slip": ItemData(0x0c, ItemClassification.filler, item_groups=["filler_battle"]),
    "Traveler's Charm": ItemData(0x70, ItemClassification.filler, item_groups=["filler_battle"]),
    "Steel Fist Sake": ItemData(0x99, ItemClassification.filler, item_groups=["filler_battle"]),
    "Steel Soul Sake": ItemData(0x9a, ItemClassification.filler, item_groups=["filler_battle"]),
    "Godly Charm": ItemData(0x9b, ItemClassification.filler, item_groups=["filler_battle"]),

    ## Ink and health Items 46, 10 %
    "Inkfinity Stone": ItemData(0x0d, ItemClassification.filler, item_groups=["filler_health_ink"]),
    "Holy Bone L": ItemData(0x04, ItemClassification.filler, item_groups=["filler_health_ink"]),
    "Holy Bone S": ItemData(0x8F, ItemClassification.filler, item_groups=["filler_health_ink"]),
    "Holy Bone M": ItemData(0x8e, ItemClassification.filler, item_groups=["filler_health_ink"]),

    ## FeedBags 65, 14%
    "Feedbag (Meat)": ItemData(0x90, ItemClassification.filler, item_groups=["filler_feedbags"]),
    "Feedbag (Herbs)": ItemData(0x91, ItemClassification.filler, item_groups=["filler_feedbags"]),
    "Feedbag (Seeds)": ItemData(0x92, ItemClassification.filler, item_groups=["filler_feedbags"]),
    "Feedbag (Fish)": ItemData(0x93, ItemClassification.filler, item_groups=["filler_feedbags"]),

    ## Treasures 241, 52 %
    ### CHEAP (<5K yen) 36 %
    "Rat Statue": ItemData(0xa6, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3300
    "Bull Horn": ItemData(0xa7, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3000
    "Incense Burner": ItemData(0xa3, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 2000
    "Vase": ItemData(0xa4, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 1900
    "Lacquerware Set": ItemData(0xaa, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 2500
    "Wooden Bear": ItemData(0xab, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 1500
    "Glass Beads": ItemData(0xad, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 1000
    "Dragonfly Bead": ItemData(0xae, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 1100
    "Coral Fragment": ItemData(0xb0, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 1700
    "Bull Statue": ItemData(0xb4, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3400
    "Tiger Statue": ItemData(0xb5, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3500
    "Rabbit Statue": ItemData(0xb6, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3600
    "Dragon Statue": ItemData(0xb7, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3700
    "Snake Statue": ItemData(0xb8, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3800
    "Horse Statue": ItemData(0xb9, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 3900
    "Sheep Statue": ItemData(0xba, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 4000
    "Monkey Statue": ItemData(0xbb, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 4100
    "Rooster Statue": ItemData(0xbc, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 4200
    "Dog Statue": ItemData(0xbd, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 4300
    "Boar Statue": ItemData(0xbe, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 4400
    "Cat Statue": ItemData(0xbf, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 4500
    "Crystal": ItemData(0xb1, ItemClassification.filler, item_groups=["filler_treasure_cheap"]),  # 5000

    ### MEDIUM (5K ~ 10K), 42, 9%
    "Pearl": ItemData(0xb2, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 5500
    "Ruby Tassels": ItemData(0xb3, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 9000
    "Turquoise Tassels": ItemData(0xc2, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 8500
    "Agate Tassels": ItemData(0xc3, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 8000
    "Amber Tassels": ItemData(0xc4, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 6500
    "Cat's Eye Tassels": ItemData(0xc5, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 7500
    "Amethyst Tassels": ItemData(0xc6, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 6000
    "Jade Tassels": ItemData(0xc7, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 7000
    "Sapphire Tassels": ItemData(0xc0, ItemClassification.filler, item_groups=["filler_treasure_medium"]),  # 9500

    ### EXPENSIVE (>10K) 33, 5%
    "White porcelain pot": ItemData(0xA0, ItemClassification.filler, item_groups=["filler_treasure_expensive"]),
    # 15000
    "Kutani Pottery": ItemData(0xa1, ItemClassification.filler, item_groups=["filler_treasure_expensive"]),  # 12000
    "Silver Pocket Watch": ItemData(0xa5, ItemClassification.filler, item_groups=["filler_treasure_expensive"]),
    # 30000
    "Etched Glass": ItemData(0xa9, ItemClassification.filler, item_groups=["filler_treasure_expensive"]),  # 20000
    "Emerald Tassels": ItemData(0xc1, ItemClassification.filler, item_groups=["filler_treasure_expensive"]),  # 10500

}

# Items that represent IG Events or quest progression.
# All items in the sections below should have a count of 0, they're created by other means:
event_items = {
    # CANINE WARRIORS STUFF
    "Satomi Power Orb (Rei)": ItemData(0x303, ItemClassification.progression, count_in_pool=0,
                                       item_groups=["canine_warriors"]),
    "Satomi Power Orb (Shin)": ItemData(0x304, ItemClassification.progression, count_in_pool=0,
                                        item_groups=["canine_warriors"]),
    "Satomi Power Orb (Chi)": ItemData(0x305, ItemClassification.progression, count_in_pool=0,
                                       item_groups=["canine_warriors"]),
    "Satomi Power Orb (Ko)": ItemData(0x306, ItemClassification.progression, count_in_pool=0,
                                      item_groups=["canine_warriors"]),
    "Satomi Power Orb (Tei)": ItemData(0x307, ItemClassification.progression, count_in_pool=0,
                                       item_groups=["canine_warriors"]),
    "Satomi Power Orb (Loyalty)": ItemData(0x4e, ItemClassification.progression, count_in_pool=0,
                                           item_groups=["canine_warriors"]),
    "Satomi Power Orb (Justice)": ItemData(0x4f, ItemClassification.progression, count_in_pool=0,
                                           item_groups=["canine_warriors"]),
    "Satomi Power Orb (Duty)": ItemData(0x50, ItemClassification.progression, count_in_pool=0,
                                        item_groups=["canine_warriors"]),

    "Serpent Crystal": ItemData(0x308, ItemClassification.progression, count_in_pool=0),
    # MOON CAVE
    "Ogre Liver": ItemData(0x4a, ItemClassification.progression, item_groups=["soup_ingredients"]),
    "Ice Lips": ItemData(0x4b, ItemClassification.progression, item_groups=["soup_ingredients"]),
    "Fire Eye": ItemData(0x4c, ItemClassification.progression, item_groups=["soup_ingredients"]),
    "Black Demon Horn": ItemData(0x4d, ItemClassification.progression, item_groups=["soup_ingredients"]),
}
weapons_items = {
    DivineInstruments.DIVINE_RETRIBUTION.value: ItemData(0x10, ItemClassification.progression, count_in_pool=0,
                                                         item_groups=["mirror_any", "divine_instrument_any"]),
    DivineInstruments.SNARLING_BEAST.value: ItemData(0x11, ItemClassification.progression, count_in_pool=0,
                                                     item_groups=["divine_instrument_2+", "mirror_any",
                                                                  "divine_instrument_any"]
                                                     ),
    DivineInstruments.INFINITY_JUDGE.value: ItemData(0x12, ItemClassification.progression, count_in_pool=0,
                                                     item_groups=["divine_instrument_3+", "divine_instrument_2+",
                                                                  "mirror_any",
                                                                  "divine_instrument_any"]),
    DivineInstruments.TRINITY_MIRROR.value: ItemData(0x13, ItemClassification.progression, count_in_pool=0,
                                                     item_groups=["divine_instrument_4+", "divine_instrument_3+",
                                                                  "divine_instrument_2+", "mirror_any",
                                                                  "divine_instrument_any"]
                                                     ),
    DivineInstruments.SOLAR_FLARE.value: ItemData(0x14, ItemClassification.progression, count_in_pool=0,
                                                  item_groups=["divine_instrument_5", "divine_instrument_4+",
                                                               "divine_instrument_3+",
                                                               "divine_instrument_2+", "mirror_any",
                                                               "divine_instrument_any"]
                                                  ),
    DivineInstruments.DEVOUT_BEADS.value: ItemData(0x15, ItemClassification.progression, count_in_pool=0,
                                                   item_groups=["rosary_any", "divine_instrument_any"]),
    DivineInstruments.LIFE_BEADS.value: ItemData(0x16, ItemClassification.progression, count_in_pool=0,
                                                 item_groups=["divine_instrument_2+", "rosary_any",
                                                              "divine_instrument_any"]),
    DivineInstruments.EXORCISM_BEADS.value: ItemData(0x17, ItemClassification.progression, count_in_pool=0,
                                                     item_groups=["divine_instrument_3+", "divine_instrument_2+",
                                                                  "rosary_any",
                                                                  "divine_instrument_any"]),
    DivineInstruments.RESURRECTION_BEADS.value: ItemData(0x18, ItemClassification.progression, count_in_pool=0,
                                                         item_groups=["divine_instrument_4+", "divine_instrument_3+",
                                                                      "divine_instrument_2+", "rosary_any",
                                                                      "divine_instrument_any"]),
    DivineInstruments.TUNDRA_BEADS.value: ItemData(0x19, ItemClassification.progression, count_in_pool=0,
                                                   item_groups=["divine_instrument_5", "divine_instrument_4+",
                                                                "divine_instrument_3+",
                                                                "divine_instrument_2+", "rosary_any",
                                                                "divine_instrument_any"]),
    DivineInstruments.TSUMUGARI.value: ItemData(0x1A, ItemClassification.progression, count_in_pool=0,
                                                item_groups=["sword_any", "divine_instrument_any"]),
    DivineInstruments.SEVEN_STRIKE.value: ItemData(0x1B, ItemClassification.progression, count_in_pool=0,
                                                   item_groups=["divine_instrument_2+", "sword_any",
                                                                "divine_instrument_any"]),
    DivineInstruments.BLADE_OF_KUSANAGI.value: ItemData(0x1C, ItemClassification.progression, count_in_pool=0,
                                                        item_groups=["divine_instrument_3+", "divine_instrument_2+",
                                                                     "sword_any",
                                                                     "divine_instrument_any"]),
    DivineInstruments.EIGHT_WONDER.value: ItemData(0x1D, ItemClassification.progression, count_in_pool=0,
                                                   item_groups=["divine_instrument_4+", "divine_instrument_3+",
                                                                "divine_instrument_2+", "sword_any",
                                                                "divine_instrument_any"]),
    DivineInstruments.THUNDER_EDGE.value: ItemData(0x1E, ItemClassification.progression, count_in_pool=0,
                                                   item_groups=["divine_instrument_5", "divine_instrument_4+",
                                                                "divine_instrument_3+",
                                                                "divine_instrument_2+", "sword_any",
                                                                "divine_instrument_any"]),
}
progressive_weapons = {
    "Progressive Mirror": ItemData(0x300, ItemClassification.progression_skip_balancing, count_in_pool=0,
                                   item_groups=["mirror_any", "divine_instrument_any"]),
    "Progressive Rosary": ItemData(0x301, ItemClassification.progression_skip_balancing, count_in_pool=0,
                                   item_groups=["rosary_any", "divine_instrument_any"]),
    "Progressive Sword": ItemData(0x302, ItemClassification.progression_skip_balancing, count_in_pool=0,
                                  item_groups=["sword_any", "divine_instrument_any"])
}
# classified as useful so they're ignored for junk fill
karmic_transformers = {
    "Karmic Returner": ItemData(0xc8, ItemClassification.useful, count_in_pool=0),
    "Karmic Transformer 1": ItemData(0x5b, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 2": ItemData(0xc9, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 3": ItemData(0x79, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 4": ItemData(0xcf, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 5": ItemData(0xcb, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 6": ItemData(0xca, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 7": ItemData(0x7b, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 8": ItemData(0x7a, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"]),
    "Karmic Transformer 9": ItemData(0x7c, ItemClassification.useful, count_in_pool=0,
                                     item_groups=["karmic_transformers"])
}

fish_table = {
    "Supreme Tuna": ItemData(0xD0, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Mountain Trout": ItemData(0xD1, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Red Snapper": ItemData(0xD2, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Striped Snapper": ItemData(0xD3, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Salmon": ItemData(0xD4, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Koi": ItemData(0xD5, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Huchen": ItemData(0xD6, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Robalo": ItemData(0xD7, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Black Bass": ItemData(0xD8, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Clownfish": ItemData(0xD9, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Bonito": ItemData(0xDA, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Yellowtail": ItemData(0xDB, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Sweetfish": ItemData(0xDC, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Trout": ItemData(0xDD, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Smelt": ItemData(0xDE, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Killifish": ItemData(0xDF, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Flying Fish": ItemData(0xE0, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Sturgeon": ItemData(0xE1, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Sunfish": ItemData(0xE2, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Freshwater Eel": ItemData(0xE3, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Loach": ItemData(0xE4, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Moray": ItemData(0xE5, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Oarfish": ItemData(0xE6, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Monkfish": ItemData(0xE7, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Catfish": ItemData(0xE8, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Giant Catfish": ItemData(0xE9, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Goby": ItemData(0xEA, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Lobster": ItemData(0xEB, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Crawfish": ItemData(0xEC, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Scallop": ItemData(0xED, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Nautilus": ItemData(0xEE, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Manta": ItemData(0xEF, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Blowfish": ItemData(0xF0, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "River Crab": ItemData(0xF1, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Starfish": ItemData(0xF2, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Loggerhead Turtle": ItemData(0xF4, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Sea Horse": ItemData(0xF5, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Octopus": ItemData(0xF6, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    "Squid": ItemData(0xF7, ItemClassification.filler, item_groups=["fishes", "filler_fishes"]),
    # TODO: Check which of those are taken into account by the game without changing anything
    "Marlin": ItemData(0xF3, ItemClassification.filler, item_groups=["fishes"]),
    "Giant Salmon": ItemData(0xCE, ItemClassification.filler, item_groups=["fishes"]),
    "Whopper": ItemData(0xFE, ItemClassification.filler, item_groups=["fishes"]),
    "Cutlass Fish": ItemData(0xFF, ItemClassification.filler, item_groups=["fishes"]),
}

food_table = {
    "Peach": ItemData(0x20, ItemClassification.filler, item_groups=["filler_food"]),
    "Apple": ItemData(0x21, ItemClassification.filler, item_groups=["filler_food"]),
    "Orange": ItemData(0x22, ItemClassification.filler, item_groups=["filler_food"]),
    "Baked Oranges": ItemData(0x23, ItemClassification.filler, item_groups=["filler_food"]),
    "Radish": ItemData(0x24, ItemClassification.filler, item_groups=["filler_food"]),
    "Turnip": ItemData(0x25, ItemClassification.filler, item_groups=["filler_food"]),
    "Ginseng": ItemData(0x26, ItemClassification.filler, item_groups=["filler_food"]),
    "Cabbage": ItemData(0x27, ItemClassification.filler, item_groups=["filler_food"]),
    "Chinese Cabbage": ItemData(0x28, ItemClassification.filler, item_groups=["filler_food"]),
    "Cherry Cake": ItemData(0x29, ItemClassification.filler, item_groups=["filler_food"]),
    "Potato": ItemData(0x2A, ItemClassification.filler, item_groups=["filler_food"]),
    "Watermelon": ItemData(0x2B, ItemClassification.filler, item_groups=["filler_food"]),
    "Bale of Rice": ItemData(0x2C, ItemClassification.filler, item_groups=["filler_food"]),
    "Roasted Meat": ItemData(0x2D, ItemClassification.filler, item_groups=["filler_food"]),
    "Bamboo Shoot": ItemData(0x2E, ItemClassification.filler, item_groups=["filler_food"]),
    "Roasted Fish": ItemData(0x2F, ItemClassification.filler, item_groups=["filler_food"]),
    "Rice Balls": ItemData(0x30, ItemClassification.filler, item_groups=["filler_food"]),
    "Dumplings": ItemData(0x31, ItemClassification.filler, item_groups=["filler_food"]),
    "Grapes": ItemData(0x32, ItemClassification.filler, item_groups=["filler_food"]),
    "Gourd": ItemData(0x33, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Rice": ItemData(0x34, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Fish": ItemData(0x35, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Egg Rolls": ItemData(0x36, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Meat": ItemData(0x37, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Crab": ItemData(0x38, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Fruit": ItemData(0x39, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Dumplings": ItemData(0x3A, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Hotchpotch": ItemData(0x3B, ItemClassification.filler, item_groups=["filler_food"]),
    "Sasa Cake": ItemData(0x3C, ItemClassification.filler, item_groups=["filler_food"]),
    "Rice Stew": ItemData(0x3D, ItemClassification.filler, item_groups=["filler_food"]),
    "Millet Dumplings": ItemData(0x3E, ItemClassification.filler, item_groups=["filler_food"]),
    "Kamiki Orange": ItemData(0x3F, ItemClassification.filler, item_groups=["filler_food"]),
    "Sashimi": ItemData(0x94, ItemClassification.filler, item_groups=["filler_food"]),
    "Golden Peach": ItemData(0x0f, ItemClassification.filler, item_groups=["filler_food"]),
}

item_table = {
    **brush_techniques_items,
    **equips,
    **bitable_items,
    **useful_items,
    **quest_items,
    **filler_items,
    **quest_items,
    **event_items,
    **weapons_items,
    **progressive_weapons,
    **karmic_transformers,
    **fish_table,
    **food_table
}

global_local_items = [
    LocalItem(["Vista of the Gods"],
              [RegionNames.KAMIKI_VILLAGE, RegionNames.KAMIKI_ISLANDS, RegionNames.KUSHIS_HOUSE,
               RegionNames.ORANGES_HOUSE],
              is_biteable=True
              ),
    LocalItem(["Tsuta Ruins Key"],
              [RegionNames.AGATA_COMMON_LOGIC, RegionNames.AGATA_FOREST],
              is_biteable=True
              ),
    LocalItem(["Mask"], [RegionNames.CALCIFIED_CAVERN], is_biteable=False,
              exclude_locations=["Calcified Cavern - Freestanding item"]),
    LocalItem(["Lucky Mallet"], [RegionNames.SUNKEN_SHIP_TREASURE], is_biteable=False),
]
soup_ingredient_local_items = LocalItem(["Ogre Liver",
                                         "Ice Lips",
                                         "Fire Eye",
                                         "Black Demon Horn"], [RegionNames.MOON_CAVE,
                                                               RegionNames.MOON_CAVE_1F_LOCKED_CAVE,
                                                               RegionNames.MOON_CAVE_1F_LOCKED_CAVE_BACK,
                                                               RegionNames.MOON_CAVE_2F_GEYSER_RAFTER,
                                                               RegionNames.MOON_CAVE_3F,
                                                               RegionNames.MOON_CAVE_B1F_LAKE,
                                                               RegionNames.MOON_CAVE_B1F_UNDER_LIFT,
                                                               RegionNames.MOON_CAVE_B2F_LIFT,
                                                               RegionNames.MOON_CAVE_B2F_FROZEN_STATUE,
                                                               RegionNames.MOON_CAVE_B2F_OTHER_LIFT,
                                                               RegionNames.MOON_CAVE_B2F_BOMBABLE,
                                                               RegionNames.MOON_CAVE_KITCHEN_BACK,
                                                               RegionNames.MOON_CAVE_3F_FIRE_EYE,
                                                               RegionNames.MOON_CAVE_3F_SAND,
                                                               RegionNames.MOON_CAVE_2F_SAND_PIT,
                                                               RegionNames.MOON_CAVE_3F_RAFTERS_AFTER_SAND,
                                                               RegionNames.MOON_CAVE_2F_RAFTERS_CHEST,
                                                               RegionNames.MOON_CAVE_4F_RAFTERS,
                                                               RegionNames.MOON_CAVE_4F_CANON,
                                                               RegionNames.MOON_CAVE_4F_AFTER_CANON], is_biteable=False,
                                        prefill_name="Soup Ingredients")
