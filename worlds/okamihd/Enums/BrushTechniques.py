from typing import TYPE_CHECKING
from enum import StrEnum


if TYPE_CHECKING:
    from .. import OkamiWorld

class BrushTechniques(StrEnum):
    # MAIN
    SUNRISE = "Sunrise"
    REJUVENATION = "Rejuvenation"
    POWER_SLASH = "Progressive Power Slash"
    CHERRY_BOMB = "Progressive Cherry Bomb"
    GREENSPROUT_BLOOM =  "Greensprout (Bloom)"
    GREENSPROUT_WATERLILY = "Greensprout (Waterlily)"
    GREENSPROUT_VINE = "Greensprout (Vine)"
    WATERSPROUT = "Watersprout"
    CRESCENT = "Crescent"
    GALESTROM = "Galestrom"
    INFERNO = "Inferno"
    VEIL_OF_MIST = "Veil of Mist"
    CATWALK = "Catwalk"
    THUNDERSTORM = "Thunderstorm"
    BLIZZARD = "Blizzard"
    ## UPGRADES/SECRET
    MIST_WARP = "Mist Warp"
    FIREBURST = "Fireburst"
    WHIRLWIND = "Whirlwind"
    DELUGE = "Deluge"
    FOUNTAIN = "Fountain"
    THUNDERBOLT = "Thunderbolt"
    ## VERY SECRET ONE
    ## I think this is the only "optional" one, every other one is required at least to clear its tutorial ?
    ICESTORM = "Icestorm"
