from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Rules import gale_shrine_access
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.KUSA_VILLAGE: [ExitData('Enter Blockhead cave', RegionNames.KUSA_VILLAGE_BLOCKHEAD,
                                        has_events=['Kusa Village - Defeat Blockhead']),
                               ExitData("Enter Mr Bamboo's house", RegionNames.BAMBOO_HOUSE),
                               ExitData("Enter Kusa Village Inn", RegionNames.KUSA_INN),
                               ExitData("Enter Gale Shrine", RegionNames.GALE_SHRINE_ENTRANCE)]
}
events = {
    RegionNames.KUSA_VILLAGE: {
        "Kusa Village - Defeat Blockhead": EventData(precollected=lambda o: o.RemoveBlockHead),
        "Kusa Village - Save Rei": EventData(id=128, cherry_bomb_level=1,
                                             is_event_item=lambda o: o.CanineRewards != 0,
                                             progress_type=lambda
                                                 o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                             else LocationProgressType.DEFAULT, event_item_name="Save Rei"),
        "Kusa Village - Save Shin": EventData(id=129, required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM],
                                              is_event_item=lambda o: o.CanineRewards != 0,
                                              progress_type=lambda
                                                  o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                              else LocationProgressType.DEFAULT, event_item_name="Save Shin"),
        "Kusa Village - Save Chi": EventData(id=130, power_slash_level=1,
                                             is_event_item=lambda o: o.CanineRewards != 0,
                                             progress_type=lambda
                                                 o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                             else LocationProgressType.DEFAULT, event_item_name="Save Chi"),
        "Kusa Village - Save Ko": EventData(id=131, required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE],
                                            is_event_item=lambda o: o.CanineRewards != 0,
                                            progress_type=lambda
                                                o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                            else LocationProgressType.DEFAULT, event_item_name="Save Ko"),
        # Should we add more conditions to get this one ?
        "Kusa Village - Save Tei": EventData(id=132, mandatory_enemies=[OkamiEnnemies.TEI],
                                             is_event_item=lambda o: o.CanineRewards != 0,
                                             progress_type=lambda
                                                 o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                             else LocationProgressType.DEFAULT, event_item_name="Save Tei")
    }
}
locations = {
    RegionNames.KUSA_VILLAGE: {
        "Kusa Village - Chest on rafters after banners": LocData(116,
                                                                 required_brush_techniques=[BrushTechniques.GALESTORM,
                                                                                            BrushTechniques.GREENSPROUT_VINE]),
        "Kusa Village - Chest on rafters before banners": LocData(117,
                                                                  required_brush_techniques=[
                                                                      BrushTechniques.GREENSPROUT_VINE]),
        "Kusa Village - Stray Bead Chest on rafters after banners": LocData(118,
                                                                            required_brush_techniques=[
                                                                                BrushTechniques.GALESTORM,
                                                                                BrushTechniques.GREENSPROUT_VINE]),
        "Kusa Village - Buried Chest near Fuse's house": LocData(120, type=LocationType.BURIED_CHEST),
        "Kusa Village - Buried Chest near Gale Shrine Ledge": LocData(121, type=LocationType.BURIED_CHEST),
        "Kusa Village - Underwater Chest near Fuse's house right": LocData(122, type=LocationType.UNDERWATER_CHEST),
        "Kusa Village - Underwater Chest near Fuse's house left": LocData(123, type=LocationType.UNDERWATER_CHEST)
    },
    RegionNames.KUSA_INN: {
        "Kusa Village - Daruma inside Inn": LocData(124, type=LocationType.DARUMA)
    },
    RegionNames.KUSA_VILLAGE_BLOCKHEAD: {
        "Kusa Village - Chest inside Blockhead Cave": LocData(115)
    },
    RegionNames.BAMBOO_HOUSE: {
        "Kusa Village - Buried Chest inside Mr Bamboo's house": LocData(119, type=LocationType.BURIED_CHEST)
    }
}
