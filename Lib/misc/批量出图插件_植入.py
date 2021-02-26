# -*- coding:cp936 -*-
import arcpy,os

# 设置需要出图mxd文档文件目录
# path1 = arcpy.GetParameterAsText(0)
path1 = ur"G:\内江市\市中区分布图\MXD"

# 设置分辨率
# res = arcpy.GetParameterAsText(1)
res = 300
# 可以进行覆盖
arcpy.env.overwriteOutput = True

for afile in os.listdir(path1):
    if afile[-3:].lower() == 'mxd':
        mxd1 = arcpy.mapping.MapDocument(os.path.join(path1,afile))
        print "正在出图..."
        
        # ExportToJEPG的第二个参数是导出图片的名称和目录设置
        arcpy.mapping.ExportToJPEG(mxd1,os.path.join(path1,afile[:-3] + 'jpg'),resolution = res) 
        # arcpy.AddMessage(afile[:-4]+"导出成功！")
        
        del mxd1
        print afile,'Done'
    else:
        print "\n非MXD文件,跳过"
