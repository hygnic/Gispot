# -*- coding:cp936 -*-
import arcpy,os

# 需要出图mxd文档文件目录
path1 = raw_input('输入地图文档目录：')
# path1 = r'G:\古蔺县'
path2 = r'G:\公示图出图2019\安居区\成果OKOK\2\图片'

# 源数据库目录
path3 = r'G:\公示图出图2019\安居区\出图2.gdb'

# 设置分辨率
res = raw_input('设置分辨率：')
res = int(res)

# 可以进行覆盖
arcpy.env.overwriteOutput = True

for afile in os.listdir(path1):
    if afile[-3:].lower() == 'mxd':
        print "\n检查正确"
        mxd1 = arcpy.mapping.MapDocument(os.path.join(path1,afile))
        
        # 更新修复数据
        
        #for lyr1 in arcpy.mapping.ListLayers(mxd1):
           # if lyr1.isBroken == True:
            #    lyr1.findAndReplaceWorkspacePath('',path3)
               
            # houzui = afile[-3].lower() + "jpg"
        #print '数据修复完成\n'
        #mxd1.save()
        print '开始出图'
        # ExportToJEPG的第二个参数是导出图片的名称和目录设置
        arcpy.mapping.ExportToJPEG(mxd1,os.path.join(path1,afile[:-3] + 'jpg'),resolution = res) 
        print afile + ' 出图完成'
        
        del mxd1
    else:
        print '\n非地图文档，跳过'
