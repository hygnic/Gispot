#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/4/3 16:15
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/3/26 16:52
# Reference:https://gis.stackovernet.com/cn/q/4179
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
#
# Write a polygon feature class
#

import os
import arcpy



def makepoly(coord_list, SR=None):
    """Convert a Python list of coordinates to an ArcPy polygon feature

    Author: Curtis Price, USGS, cprice@usgs.gov

    Examples, from Desktop Help 10.x: Reading Geometries

    Feat0 = [
            [[3.0, 8.0],
            [1.0, 8.0],
            [2.0, 10.0],
            [3.0, 8.0]]
            ]
    Feat1 = [
            [[5.0, 3.0],
            [3.0, 3.0],
            [3.0, 5.0],
            [5.0, 3.0]],

            [[7.0, 5.0],
            [5.0, 5.0],
            [5.0, 7.0],
            [7.0, 5.0]],
            ]

            # this feature has an interior ring (donut)

            Feat2 = [
            [[9.0, 11.0],
            [9.0, 8.0],
            [6.0, 8.0],
            [6.0, 11.0],
            [9.0, 11.0],
            None,
            [7.0, 10.0],
            [7.0, 9.0],
            [8.0, 9.0],
            [8.0, 10.0],
            [7.0, 10.0]]
            ]
"""
    
    parts = arcpy.Array()
    rings = arcpy.Array()
    ring = arcpy.Array()
    for part in coord_list:
        for pnt in part:
            if pnt:
                ring.add(arcpy.Point(pnt[0], pnt[1]))
            else:
                # null point - we are at the start of a new ring
                rings.add(ring)
                ring.removeAll()
        # we have our last ring, add it
        rings.add(ring)
        ring.removeAll()
        # if we only have one ring: remove nesting
        if len(rings) == 1:
            rings = rings.getObject(0)
        parts.add(rings)
        rings.removeAll()
    # if single-part (only one part) remove nesting
    if len(parts) == 1:
        parts = parts.getObject(0)
    return arcpy.Polygon(parts, SR)


# test data from:
# Desktop Help 10.0: Reading Geometries

Feat0 = [
    [[3.0, 8.0],
     [1.0, 8.0],
     [2.0, 10.0],
     [3.0, 8.0]]
]
Feat1 = [
    [[5.0, 3.0],
     [3.0, 3.0],
     [3.0, 5.0],
     [5.0, 3.0]],
    
    [[7.0, 5.0],
     [5.0, 5.0],
     [5.0, 7.0],
     [7.0, 5.0]],
]

# this last feature has an interior ring (donut)

Feat2 = [
    [[9.0, 11.0],
     [9.0, 8.0],
     [6.0, 8.0],
     [6.0, 11.0],
     [9.0, 11.0],
    
     [7.0, 10.0],
     [7.0, 9.0],
     [8.0, 9.0],
     [8.0, 10.0],
     [7.0, 10.0]],
    
    [[6.5, 10.8],
     [6.8, 10.8],
     [6.8, 10.2],
     [6.2, 9.9],
     [6.5, 10.8]],
    
    [[7.2, 9.7],
     [7.7, 9.7],
     [7.7, 9.2],
     [7.2, 9.1],
     ]
]

# test code

# create the empty feature class

# with real data, provide a SR code, name or dataset for SR
# SR = arcpy.SpatialReference(4326)
SR = None
# env.workspace = env.scratchGDB  # C:\Users\Administrator\AppData\Local\Temp\scratch.gdb
# env.workspace = "%scratchGDB%" # C:\Users\Administrator\AppData\Local\Temp\scratch.gdb

arcpy.env.workspace = ur"G:\MoveOn\MyPython\2020\NumPY_edu\files\Folder"
Data = arcpy.CreateScratchName("", "", "featureclass", arcpy.env.workspace)
print "writing: " + Data
print
arcpy.CreateFeatureclass_management(os.path.dirname(Data),
                                    os.path.basename(Data), "Polygon",
                                    spatial_reference=SR)

# create the polygons and write them
Rows = arcpy.da.InsertCursor(Data, "SHAPE@")
for f in [Feat0, Feat1, Feat2]:
    print "coords: " + repr(f)
    p = makepoly(f)
    print "feature: " + repr(p)
    Rows.insertRow([p])
del Rows