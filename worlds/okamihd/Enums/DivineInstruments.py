from typing import TYPE_CHECKING, NamedTuple
from enum import Enum, StrEnum

from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from .. import OkamiWorld


class DivineInstruments(StrEnum):
    # MIRRORS
    DIVINE_RETRIBUTION = "Divine Retribution"
    SNARLING_BEAST = "Snarling Beast"
    INFINITY_JUDGE = "Infinity Judge"
    TRINITY_MIRROR = "Trinity Mirror"
    SOLAR_FLARE = "Solar Flare"

    # ROSARIES
    DEVOUT_BEADS = "Devout Beads"
    LIFE_BEADS = "Life Beads"
    EXORCISM_BEADS = "Exorcism Beads"
    RESURRECTION_BEADS = "Resurrection Beads"
    TUNDRA_BEADS = "Tundra Beads"

    # SWORDS
    TSUMUGARI = "Tsumugari"
    SEVEN_STRIKE = "Seven Strike"
    BLADE_OF_KUSANAGI = "Blade of Kusanagi"
    EIGHT_WONDER = "Eight Wonder"
    THUNDER_EDGE = "Thunder Edge"
