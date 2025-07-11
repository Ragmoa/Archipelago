from typing import TYPE_CHECKING, NamedTuple
from enum import StrEnum

from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from .. import OkamiWorld

class RegionNames(StrEnum):
    MENU = "Menu"

    # Eastern Nippon

    ## Cursed Kamiki
    CURSED_KAMIKI = "Cursed Kamiki"

    ## River of the Heavens
    RIVER_OF_THE_HEAVENS_KAMIKI = "River of the Heavens (Kamiki side)"
    RIVER_OF_THE_HEAVENS_NAGI = "River of the Heavens (Nagi side)"

    ## Cave of Nagi
    CAVE_OF_NAGI = "Cave of Nagi"
    CAVE_OF_NAGI_TACHIGAMI = "Cave of Nagi (Tachigami sequence)"

    ## Kamiki Village
    ### Exteriors
    STONE_KAMIKI = "Kamiki Village (Stone state)"
    KAMIKI_VILLAGE = "Kamiki Village"
    KAMIKI_ISLANDS = "Kamiki Village Islands"
    ### Interiors
    KUSHIS_HOUSE = "Kushi's house"
    SUSANOS_HOUSE = "Susano's house"
    SUSANOS_UNDERGROUD = "Susano's Secret Underground Meditation Chamber"
    ORANGES_HOUSE = "Mr and Mrs Orange's house"


    ## Shinshu Field
    CURSED_SHINSHU_FIELD = "Cursed Shinshu Field"
    SHINSHU_FIELD = "Shinshu Field"
    SHINSHU_FIELD_AGATA_CAVE="Shinshu Field (Cave to Agata Forest)"
    TAMA_HOUSE="Tama's house"

    ## HANA VALLEY
    CURSED_HANA_VALLEY = "Cursed Hana Valley"
    HANA_VALLEY = "Hana Valley"
    HANA_VALLEY_SAKIGAMI =" Hana Valley - Sakigami sequence"

    ## AGATA FOREST
    CURSED_AGATA_FOREST="Cursed Agata Forest"
    AGATA_FOREST_WAKA="Agata Forest (Pre-waka fight)"
    AGATA_FOREST="Agata Forest"
    ### INTERIORS
    FAWNS_HOUSE="Madame Fawn's House"

    ## TSUTA RUINS
    TSUTA_RUINS_1F_MAIN_PART="Tsuta Ruins (1F - Main Part)"
    TSUTA_RUINS_MUSHROOMS="Tsuta Ruins (Mushrooms)"
    TSUTA_RUINS_LEFT_SIDE= "Tsuta Ruins (Left Side)"
    TSUTA_RUINS_DEVIL_GATES="Tsuta Ruins (Devil Gates)"
    TSUTA_RUINS_CENTRAL_STATUE="Tsuta Ruins (Inside central Statue)"
    TSUTA_RUINS_SPIDER = "Tsuta Ruins (Spider Queen's lair)"
    ## TAKA PASS
    CURSED_TAKA_PASS="Curesd Taka Pass"
