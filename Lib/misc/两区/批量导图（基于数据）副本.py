# -*- coding: utf8 -*-#
#功能：批量自动导出两区划定公示图
#版本：1.1
#作者：曾红扬
##############################################################################
#导入包
import arcpy,os,time
import datetime

time1=datetime.datetime.now()

time2 = datetime.datetime.strptime("2019-9-1", "%Y-%m-%d")

#设置数据源文件数据库
LQDatasource = ur"G:\内江市\工作文件_lcc_19_7\内江出图\出图2.gdb"

#用户设置分辨率
res = "300"


#数据框空间参考
SR = 4544
# SR = "CGCS2000_3_Degree_GK_CM_105E"

#模板目录
one_file_path = ur"G:\内江市\工作文件_lcc_19_7\内江出图\TemplateZJ-基于选择"

#用户设置输出文件夹
layoutdir = ur"G:\内江市\工作文件_lcc_19_7\内江出图\成果2020"

#循环读取模板MXD
for afile in os.listdir(one_file_path):
#判断是否为MXD文件
   if afile[-3:].lower()=='mxd':
#读取MXD文件
    mxd=arcpy.mapping.MapDocument(os.path.join(one_file_path, afile))
#更新数据源
    for lyr in arcpy.mapping.ListLayers(mxd):
     lyr.findAndReplaceWorkspacePath('',LQDatasource)
#可选方案2
    for df in arcpy.mapping.ListDataFrames(mxd):
     df.spatialReference=SR
#遍历“出图范围”图层的所有要素
    cursor = arcpy.SearchCursor(arcpy.mapping.ListLayers(mxd,"出图范围","")[0],'')
    for row in cursor:
#依次选择要素并且缩放居中，并设置比例尺为5000，再另存MXD
     lyr = arcpy.mapping.ListLayers(mxd,"出图范围","")[0]
     a = [row.getValue('OBJECTID')]
     lyr.setSelectionSet("NEW",a)
     df = arcpy.mapping.ListDataFrames(mxd)[0]
     df.zoomToSelectedFeatures()
     df.scale = 5000
     mxd.saveACopy(layoutdir+'\\'+afile[:-4]+row.getValue('XJQYMC')+
                    row.getValue('CJQYMC')+'.mxd','10.3')
     

#遍历输出文件夹里面的MXD，并且替换文本和设置查询，最后导出JPG
for bfile in os.listdir(layoutdir):
   if bfile[-3:].lower()=='mxd':
    mxd2=arcpy.mapping.MapDocument(os.path.join(layoutdir,bfile))
    cursor = arcpy.SearchCursor(arcpy.mapping.ListLayers(mxd2,"出图范围","")[0],'')
    for row in cursor:
# 替换布局视图中的文本
     for elm in arcpy.mapping.ListLayoutElements(mxd2, "TEXT_ELEMENT"):
      if elm.text == "BT":
       elm.text = row.getValue("XZQMC")+row.getValue("XJQYMC")+row.getValue("CJQYMC")+u"“"+u"两区"+u"”"+u"划定公示图"
      if elm.text == "LQPKDM1":
       elm.text = row.getValue("标注1")
      if elm.text == "LQPKDM2":
       elm.text = row.getValue("标注2")
      if elm.text == "LQPKDM3":
       elm.text = row.getValue("标注3")
      if elm.text == "LQPKDM4":
       elm.text = row.getValue("标注4")
      if elm.text == "LQPKDM5":
       elm.text = row.getValue("标注5")
      if elm.text == "LQPKDM6":
       elm.text = row.getValue("标注6")
      if elm.text == "LQPKDM7":
       elm.text = row.getValue("标注7")
      if elm.text == "LQPKDM8":
       elm.text = row.getValue("标注8")
      if elm.text == "HCSJ":
       elm.text = row.getValue("DCRQ")
      if elm.text == "ZTY":
       elm.text = row.getValue("ZTY")
      if elm.text == "ZTSJ":
       elm.text = row.getValue("ZTRQ")
      if elm.text == "TDLYXZ":
       elm.text = "("+row.getValue("TDLYXZ")+")"
      if elm.text == "JBNT":
       elm.text = "("+row.getValue("JBNT")+")"
      if elm.text == "YGYX":
       elm.text = "("+row.getValue("YGYX")+")"

#设置每个图层的查询语句
     for lyr in arcpy.mapping.ListLayers(mxd2,"村委会"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"

     for lyr in arcpy.mapping.ListLayers(mxd2,"机井提灌站"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"

     for lyr in arcpy.mapping.ListLayers(mxd2,"两区片块"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"


     for lyr in arcpy.mapping.ListLayers(mxd2,"XZDW"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"

     for lyr in arcpy.mapping.ListLayers(mxd2,"LQDK"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"


     for lyr in arcpy.mapping.ListLayers(mxd2,"两区地块图例"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"

     for lyr in arcpy.mapping.ListLayers(mxd2,"两区地块底色"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"

     for lyr in arcpy.mapping.ListLayers(mxd2,"两区地块"):
       lyr.definitionQuery = "CJQYDM"+"="+"\'"+row.getValue("CJQYDM")+"\'"

     for lyr in arcpy.mapping.ListLayers(mxd2,"出图范围"):
       lyr.setSelectionSet("NEW",[])
#保存MXD
    mxd2.save()
#导出JPEG，文件名为：模板名字






















































