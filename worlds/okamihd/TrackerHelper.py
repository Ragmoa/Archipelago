from json import JSONEncoder
from typing import TYPE_CHECKING, Iterable, List

import BaseClasses
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


def location_exporter(world:"OkamiWorld"):
    # First we sort every region in which tracker map it'll go
    tracker_maps:dict[str, list[str]]={}
    for region in world.get_regions():
        tracker_map=match_region_with_map(region.name)
        if tracker_map is not None:
            if not tracker_map in tracker_maps:
                tracker_maps[tracker_map]=[region.name]
            else:
                tracker_maps[tracker_map].append(region.name)
        else:
            print("No tracker map found for" + region.name + "!")

    for map_name, map_regions in tracker_maps.items():
        print ("Exporting map "+ map_name)
        export_map(map_name,map_regions,world)

def export_map(map_name:str,map_regions:List[str],world:"OkamiWorld"):
    filename=map_name+'.json'
    # Build the children (1 per section with 1 item per section)
    children=[]
    for region_name in map_regions:
        reg = world.get_region(region_name)
        for l in reg.locations:
            children.append({
                "name":format_location_name_for_tracker(l),
                "section":[
                    {
                    "name": format_location_name_for_tracker(l),
                    "item_count": 1
                    }
                ],
                "map_locations":[{
                    "map":map_name,
                    # Impossible to know where we'll place the square on the tracker, so we put it on 0,0 for now.
                    # If I have to regen, how can I keep the positions of squares that have been already placed ?
                    'x':0,
                    'y':0
                }]
            })

    json_data=[{
        "name":map_name,
        "children":children
    }]

    #Export the json.

    with open(world.settings.general_options.output_path+"/tracker/"+filename,"w") as file_writer:
        file_writer.write(JSONEncoder.encode(json_data))

def get_location_json(loc:OkamiLocation)-> dict:
    return {
        "name":loc.name,
        "sections":[
            "name"
        ]
    }

def format_location_name_for_tracker(location_name:str)->str:
    return location_name.partition(' - ')[-1]