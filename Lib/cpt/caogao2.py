# -*- coding: utf8 -*-

import arcpy
a = 4544
v = "CGCS2000_3_Degree_GK_CM_108E"
mxd1 = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd1)[0]
layer = arcpy.mapping.ListLayers(mxd1)[0]
# b= arcpy.Describe(ur"E:\move on move on\公示图\公示图.mxd")
# c= b.spatialReference
# print  c
print df.spatialReference

df.spatialReference = arcpy.SpatialReference(4545)
cursor = arcpy.da.SearchCursor(layer,"OBJECTID")
for row in cursor:
	# arc_id = row[0]
	# print type(arc_id)
	# print arc_id
	# print type(row)
	# print row
	# print row
	# for field_name in row:
	# 	print field_name
	pass
	
		
cursor = arcpy.SearchCursor(layer,"")
for row in cursor:
	a = [row.getValue('OBJECTID')] # list 字段OBJECTID的list
	for b in a:
		print b

print a