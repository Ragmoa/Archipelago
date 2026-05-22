import json
import pkgutil
from typing import TYPE_CHECKING, Iterable, List, Any
import BaseClasses
from BaseClasses import Region
from Utils import output_path
from .CheckIds import is_container, get_map_and_spawn_id, is_brush_check
from .Enums.TrackerMaps import tracker_maps, custom_mappings, transformations
from .Types import OkamiLocation, LocData, TrackerMapTransform
from .RegionsData import okami_locations

if TYPE_CHECKING:
    from . import OkamiWorld


# Functions to export stuff for poptracker pacakge making

# give the corresponding map in the tracker depending on the Region
def match_region_with_map(region_name: str) -> str:
    # Check for special mapping
    tracker_map = custom_mappings.get(region_name, None)
    if tracker_map is not None:
        return tracker_map

    for a in tracker_maps:
        if region_name.startswith(a):
            return a


def location_exporter(world: "OkamiWorld"):
    # First we sort every region in which tracker map it'll go
    tracker_maps: dict[str, list[str]] = {}
    containers_file = pkgutil.get_data(__name__, "data/containers.json").decode("utf-8")
    containers = json.loads(containers_file)["levels"]
    overrides_file = pkgutil.get_data(__name__, "data/tracker_override.json").decode("utf-8")
    overrides = json.loads(overrides_file)
    for region in world.get_regions():
        tracker_map = match_region_with_map(region.name)
        if tracker_map is not None:
            if not tracker_map in tracker_maps:
                tracker_maps[tracker_map] = [region.name]
            else:
                tracker_maps[tracker_map].append(region.name)
        else:
            print("No tracker map found for " + region.name + "!")

    for map_name, map_regions in tracker_maps.items():
        print("Exporting map " + map_name)
        export_map(map_name, map_regions, containers, overrides, world)


def export_map(map_name: str, map_regions: List[str], containers: Any, overrides: Any, world: "OkamiWorld"):
    filename = map_name.replace(' ', '_') + '.json'
    # Build the children (1 per section with 1 item per section)
    children = []
    for region_name in map_regions:
        reg = world.get_region(region_name)
        # How do we pack chests together when it's needed ?
        # How do we handle merchants ? (Maybe should be seperate)
        for l in reg.locations:
            loc_data = None
            try:
                # Load the locData
                loc_data = okami_locations[reg.name][l.name]
            except KeyError:
                print("No locations for " + reg.name)
            # Check if the location is a container.  (with its id) if it is, we find its container in the container.json, to get the coordiantes of the chest
            if loc_data is not None:
                x, y = None, None
                if is_container(loc_data.id):
                    map_id,spawn_id=get_container_map_spawn_id(loc_data.id)
                    x,y =get_tracker_override_position(map_id,spawn_id,overrides)
                    if x==0 and y==0:
                        container = get_container(map_id,spawn_id, containers)
                        t = None

                        try:
                            t = transformations[map_name]
                        except KeyError:
                            print("No transformation for " + map_name)
                        if t is not None:
                            # We use the converter for the right tracker map to get the tracker coordinates
                            x, y = convert_position(transformations[map_name], container["x"], container["z"])
                        else:
                            x, y = 0, 0

                elif is_brush_check(loc_data.id):
                    x, y = get_tracker_override_position("brushes", str(loc_data.id % 1000), overrides)

                children.append({
                    "name": format_location_name_for_tracker(l.name),
                    "sections": [
                        {
                            "name": format_location_name_for_tracker(l.name),
                            "item_count": 1
                        }
                    ],
                    "map_locations": [{
                        "map": map_name,
                        'x': x,
                        'y': y
                    }]
                })

    json_data = [{
        "name": map_name,
        "children": children
    }]

    # Export the json.

    with open(output_path() + "/tracker/" + filename, "w") as file_writer:
        file_writer.write(json.dumps(json_data))


def format_location_name_for_tracker(location_name: str) -> str:
    return location_name.partition(' - ')[-1]

def get_container_map_spawn_id(container_id:int)->(str,str):
    # split the id into map and spawnid:
    map_id, spawn_id = get_map_and_spawn_id(container_id)
    map_id_hex = "0x" + "{:03x}".format(map_id)
    return map_id_hex,str(spawn_id)

def get_container(map_id_hex:str, spawn_id:str, containers: Any):
    return containers[map_id_hex]["containers"][int(spawn_id)]


def convert_position(tf: TrackerMapTransform, x: int, z: int) -> (int, int):
    return int(((x * tf.x1) + (z * tf.x2)) + tf.x_const), int(((x * tf.y1) + (z * tf.y2)) + tf.y_const)


def get_tracker_override_position(map_id: str, bit_id: str, override: Any) -> (int, int):
    try:
        ov = override[map_id][bit_id]
        return ov["x"], ov["y"]
    except KeyError:
        print("No override found for " + map_id + " " + bit_id)
        return 0,0