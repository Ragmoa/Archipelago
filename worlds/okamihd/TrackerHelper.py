from typing import TYPE_CHECKING, Iterable, List

from BaseClasses import Region
from .Enums.TrackerMaps import tracker_maps, custom_mappings
from .Types import OkamiLocation

if TYPE_CHECKING:
    from . import OkamiWorld

# Functions to export stuff for poptracker pacakge making

# give the corresponding map in the tracker depending on the Region
def match_region_with_map(region_name:str) -> str:
    # Check for special mapping
    tracker_map=custom_mappings.get(region_name,None)
    if tracker_map is not None:
        return tracker_map

    for a in tracker_maps:
        if region_name.startswith(a):
            return a


def location_exporter(regions:Iterable[Region]):
    # First we sort every region in which tracker map it'll go
    tracker_maps:dict[str, list[str]]={}
    for region in regions:
        tracker_map=match_region_with_map(region.name)
        if not tracker_map in tracker_maps:
            tracker_maps[tracker_map]=[region.name]
        else:
            tracker_maps[tracker_map].append(region.name)

    for map_name, map_regions in tracker_maps.items():
        export_map(map_name,map_regions,regions)

def export_map(map_name:str,map_regions:List[str],region:Iterable[Region]):
    filename=map_name+'.json'
    # Build the children (1 per section with 1 item per section)
    children=[]


    json_data=[{
        "name":map_name,
        "children":children
    }]

    #Export the json.

def get_location_json(loc:OkamiLocation)-> dict:
    return {
        "name":loc.name,
        "sections":[
            "name"
        ]
    }