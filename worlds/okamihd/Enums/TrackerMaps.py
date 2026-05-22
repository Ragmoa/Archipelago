from enum import StrEnum
from typing import TYPE_CHECKING

from ..Types import TrackerMapTransform

if TYPE_CHECKING:
    from .. import OkamiWorld, RegionNames

tracker_maps = {
    "Kamiki Village",
    "River of the Heavens",
    "Cave of Nagi",
    "Shinshu Field",
    "Hana Valley",
    "Agata Forest",
    "Tsuta Ruins 1F",
    "Tsuta Ruins 2F",
    "Tsuta Ruins 3F",
    "Tsuta Ruins 4F",
}

transformations={
    "Kamiki Village":TrackerMapTransform(x1=0.099849,x2=-0.00329,y1=0.001521,y2=0.099717,x_const=367.08584,y_const=460.737157),
    "Shinshu Field":TrackerMapTransform(x1=0.094684,x2=0.000595,y1=0.000134,y2=0.095882,x_const=403.668378,y_const=592.831915),
    "Agata Forest":TrackerMapTransform(x1=0.099510,x2=0.000963,y1=0.004976,y2=0.097549,x_const=598.156834,y_const=-28.082484)
}

custom_mappings={

}
