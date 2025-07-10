from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits={
}
events={

}

locations = {
    RegionNames.TAKA_PASS:{
        "Taka Pass - Chest under leaf pile near Guardian Sapling" : LocData(99, type=LocationType.BURIED_UNDER_LEAF_PILE,required_items_events=["Taka pass - Restore Bridge to Guardian Sapling"]),
        "Taka Pass - Chest on top of big rock above ledge": LocData(100,required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Taka Pass - Chest under leaf pile after cave": LocData(101,type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near cave west": LocData(102, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near Ultimate Origin mirror": LocData(103, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest on top of Gutters' House":LocData(104,required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Taka Pass - Chest across banners": LocData(105, required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE, BrushTechniques.GALESTROM]),
        "Taka Pass - Buried chest near Gutters' house":LocData(106,type=LocationType.BURIED_CHEST),
        "Taka Pass - Buried chest near mermaid spring": LocData(107, type=LocationType.BURIED_CHEST),
        "Taka Pass - Buried chest near tea house": LocData(108, type=LocationType.BURIED_CHEST),
        "Taka Pass - Buried chest near treasure hunter": LocData(109, type=LocationType.BURIED_CHEST),
        #Find a better name
        "Taka Pass - Buried under leaf pile near city checkpoint exit": LocData(110, type=LocationType.BURIED_UNDER_LEAF_PILE),
        #Find out which house
        "Taka Pass - Chest under leaf pile behind house": LocData(111, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near mermaid spring": LocData(112, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near city checkpoint exit #2": LocData(113, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near moles gang": LocData(114,type=LocationType.BURIED_UNDER_LEAF_PILE),
    }

}