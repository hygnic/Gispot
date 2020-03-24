# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/23
# python2 arcgis10.6
"""计数功能，计算当前mxd有多少个图层layer"""

import arcpy
mxd1 = arcpy.mapping.MapDocument("CURRENT")
layer_list = arcpy.mapping.ListLayers(mxd1)
for i in layer_list:
	print i.name
item_count = len(layer_list)
print item_count
msg = "\n{0} layer in current mxd\n".format(item_count)
arcpy.AddMessage(msg)
