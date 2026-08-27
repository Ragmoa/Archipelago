from typing import TYPE_CHECKING

from rule_builder.rules import True_, Has, HasAny
from ..CheckIds import container_check_id, shop_check_id
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames, MapIds
from ..Enums.WarpType import WarpType
from ..Types import ExitData, EventData, WarpData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.PONC_TAN: [
        ExitData(RegionNames.PONC_TAN_WATERFALL, required_items_events=[BrushTechniques.GREENSPROUT_VINE])
    ]
}
events = {
    RegionNames.PONC_TAN:{
        "Ponc'tan - Meet Ishaku": EventData(),
        "Ponc'tan - Meet Myia": EventData()
    }
}
locations = {
    RegionNames.PONC_TAN: {
        "Ponc'tan - Freestanding Chest on leaf behind origin mirror": LocData(container_check_id(MapIds.PONC_TAN, 0),
                                                                              required_brush_techniques=[
                                                                                  BrushTechniques.GREENSPROUT_VINE]),
        "Ponc'tan - Freestanding Chest on west leaf behind Gengo's shop": LocData(
            container_check_id(MapIds.PONC_TAN, 11)),
        "Ponc'tan - Freestanding Chest on lone northwest leaf": LocData(
            container_check_id(MapIds.PONC_TAN, 4), required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Ponc'tan - Freestanding Chest on lone northeast leaf": LocData(
            container_check_id(MapIds.PONC_TAN, 3), required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Ponc'tan - Freestanding Chest on lone southeast leaf": LocData(
            container_check_id(MapIds.PONC_TAN, 10), required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Ponc'tan - Freestanding Chest on eastern near clover": LocData(
            container_check_id(MapIds.PONC_TAN, 9)),
        "Ponc'tan - Freestanding Chest between vegetables": LocData(
            container_check_id(MapIds.PONC_TAN, 7)),
        "Ponc'tan - Freestanding Chest on platform above Gengo's shop": LocData(
            container_check_id(MapIds.PONC_TAN, 8)),

    },
    RegionNames.PONC_TAN_WATERFALL: {
        "Ponc'tan - Freestanding Chest on leaf near waterfall": LocData(
            container_check_id(MapIds.PONC_TAN, 6)),
        "Ponc'tan - Freestanding Chest on leaf above waterfall": LocData(
            container_check_id(MapIds.PONC_TAN, 5),
            special_rule=HasAny(BrushTechniques.GREENSPROUT_VINE, BrushTechniques.GREENSPROUT_VINE)),
    }
}
shop_locations = {
    RegionNames.PONC_TAN: {
        "Ponc'tan - Gengo's shop Slot 1": LocData(shop_check_id(13, 0), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 2": LocData(shop_check_id(13, 1), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 3": LocData(shop_check_id(13, 2), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 4": LocData(shop_check_id(13, 3), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 5": LocData(shop_check_id(13, 4), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 6": LocData(shop_check_id(13, 5), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 7": LocData(shop_check_id(13, 6), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 8": LocData(shop_check_id(13, 7), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 9": LocData(shop_check_id(13, 8), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 10": LocData(shop_check_id(13, 9), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 11": LocData(shop_check_id(13, 10), type=LocationType.SHOP),
        "Ponc'tan - Gengo's shop Slot 12": LocData(shop_check_id(13, 11), type=LocationType.SHOP),
    }
}
