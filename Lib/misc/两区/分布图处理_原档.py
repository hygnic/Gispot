# -*- coding: cp936 -*-
# 2019 08 15 廖晨辰

import arcpy,os,sys

# 模板目录，只需要一个设置好了的mxd文件
# template = 'G:/都江堰/都江堰分布图0815/编程试验文件/中兴镇.mxd'
template = 'CURRENT'
# template = template.decode('utf-8')

# 设置输出目录
outputclass = u'G:/南江县/南江分布图/输出地图文档'
# outputclass = outputclass.decode('utf-8')
# outputclass = outputclass.decode('gb2312')

# 设置缓冲区文件存放目录
bufferoutclass = u'G:/南江县/南江分布图/缓冲区文件'
# bufferoutclass = bufferoutclass.decode('gb2312')

# 创建数据库容纳XJQY的各个单独的区域，为缓冲区的建立做准备
tempDB = u'中间处理暂存数据库.gdb'
arcpy.CreateFileGDB_management(bufferoutclass,tempDB)

# 可以进行覆盖
arcpy.env.overwriteOutput = True

# 读取文件
mxd1 = arcpy.mapping.MapDocument(template)
print mxd1.title
dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
dataframe2 = arcpy.mapping.ListDataFrames(mxd1)[1]

# 必须将第一个图层设置为激活图层，否则退出程序
if not mxd1.activeDataFrame == '图层':
    sys.exit()
    print '激活图层错误'
    
print dataframe1.name+ u'图框读取成功'
print dataframe2.name+ u'图框读取成功'



# 匹配字段是CJQYDM
layerlist1 = ['标志牌','村名']

# 匹配字段是XJQYDM
layerlist2 = ['XJQY','乡镇驻地','村委会','DZDW','XZDW','村界']

# 匹配字段是QSDWMC1


#从该图层中读取属性表信息，将它传递与其他图层
datalayer = arcpy.mapping.ListLayers(mxd1,'XJQY',dataframe1)[0]


cursor = arcpy.da.SearchCursor(datalayer,('XJQYDM','XJQYMC','XJXZQ'))
namelist = []

# 读取XJQYDM
for row in cursor:

    getvalue_XJQYDM = row[0]
    getvalue_XJQYMC = row[1]
    getvalue_MC = row[2]
    

    # 定义查询
        # '标志牌','村名'
    for onelayerlist in layerlist1:
        layer = arcpy.mapping.ListLayers(mxd1,onelayerlist,dataframe1)[0]
        # 有时候标志牌暂时没有
        if not layer.isBroken:
            # layer.definitionQuery = ''
            layer.definitionQuery = '"' + 'CJQYDM' + '"' + ' like' \
            + " '" + getvalue_XJQYDM[:9] + "%'"
        
        # 'XJQY','乡镇驻地','村委会','DZDW','XZDW','村界'
    for onelayerlist in layerlist2:
        layer = arcpy.mapping.ListLayers(mxd1,onelayerlist,dataframe1)[0]
        # layer.definitionQuery = ''
        layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
        
        # XZDW
    # layer =  arcpy.mapping.ListLayers(mxd1,'XZDW',dataframe1)[0]   
    # layer.definitionQuery = '"' + 'QSDWDM1' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
    
    
        # 两区片块及作物类型
    layer =  arcpy.mapping.ListLayers(mxd1,'两区片块及作物类型',dataframe1)[0]   
    layer.definitionQuery = '"' + 'LQPKDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
    
        # LQDK融合
    layer =  arcpy.mapping.ListLayers(mxd1,'LQDK融合',dataframe1)[0]   
    layer.definitionQuery = '"' + 'LQDKDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
    
        # DLTB融合
    layer =  arcpy.mapping.ListLayers(mxd1,'DLTB融合',dataframe1)[0]   
    layer.definitionQuery = '"' + 'QSDWDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM +"%'"
        
        # 修改第二个图框的定义查询
    layer = arcpy.mapping.ListLayers(mxd1,'XJQY',dataframe2)[0]
    layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
    
    # 设置地图文档中的文字元素
    for elm in arcpy.mapping.ListLayoutElements(mxd1,'TEXT_ELEMENT'):
        if elm.name=='BT1':
            elm.text = u'%s%s"两区"农田空间分布图'%(getvalue_MC,getvalue_XJQYMC)
        if elm.name=='BT2':
            elm.text = u'%s在%s的位置示意图'%(getvalue_XJQYMC,getvalue_MC)


    # 缩放
    # 缩放至图层
    layer = arcpy.mapping.ListLayers(mxd1,'XJQY',dataframe1)[0]
    dataframe1.extent = layer.getSelectedExtent()
    dataframe2.scale = 10000

    
    arcpy.env.workspace = bufferoutclass
    # 将选择的数据导入进数据库中
    arcpy.FeatureClassToGeodatabase_conversion(datalayer,bufferoutclass + '/' + tempDB)
    # 将数据库中文件重命名
    prename = bufferoutclass+'/'+tempDB+'/'+'GPL0'
    arcpy.Rename_management(prename,getvalue_XJQYMC)
    
    
    namelist.append(getvalue_XJQYMC)
    
    # 输出地图文档
    mxd1.saveACopy(outputclass+'/'+getvalue_XJQYMC+'.mxd')
del cursor
print 'raw_mxd saved!'

# 排序列表
namelist.sort()



arcpy.env.workspace = bufferoutclass

    
    
for aname in namelist:

   
    # 生成缓冲区
    inFeatures = tempDB + '/' + aname
    outFeatureClass = bufferoutclass + '/' + aname
    distance = [30,60,90]
    bufferunit = 'meters'
    arcpy.MultipleRingBuffer_analysis(inFeatures,outFeatureClass,distance,bufferunit,'','','OUTSIDE_ONLY')
    
    dellayer = arcpy.mapping.ListLayers(mxd1,'',dataframe1)[0]
    arcpy.mapping.RemoveLayer(dataframe1,dellayer)
print 'buffer completed!'
    
# 让刚刚生成的环形缓冲区文件替换个乡镇mxd中的'缓冲区'图层
    # 读取生成的地图文档
    

for newfile in os.listdir(outputclass):
    # 将名字选出来
    xxxx = newfile[:-4]
    newMXD = arcpy.mapping.MapDocument(os.path.join(outputclass,newfile))
    newlayer = arcpy.mapping.ListLayers(newMXD,'缓冲区')[0]
    # 将与mxd文档名字相同的缓冲区替换进去
    newlayer.replaceDataSource(bufferoutclass,'SHAPEFILE_WORKSPACE',xxxx)
    newMXD.save()

print 'mxd saved!'

# 保存其它版本


    


'''
# 生成缓冲区
inFeatures = tempDB + '/' + 'GPL0'
outFeatureClass = getvalue_XJQYMC + u'环形缓冲区'
distance = [30,60,90]
bufferunit = 'meters'
arcpy.MultipleRingBuffer_analysis(inFeatures,outFeatureClass,distance,bufferunit,'','','OUTSIDE_ONLY')

# 替换文件
    # 让刚刚生成的环形缓冲区文件替换模板中的'缓冲区'图层
infile = outFeatureClass
datalayer1.replaceDataSource(bufferoutclass,'SHAPEFILE_WORKSPACE',infile)
print 'replace!'

# 将画面缩放至所选图形
datalayer1.getExtent()
'''
# 生成缓冲区


'''
# 使用该方法时，会自动移除当前地图文档中的XJQY，导致报错000732（文件缺失），暂不清楚错误原因，可能与编码格式和字体有关系

# arcpy.env.workspace = u'G:/都江堰/都江堰分布图0815/出图数据'

# inFeatures = u'G:/都江堰/都江堰分布图0815/行政区/乡界面1.shp'
inFeatures = datalayer
# 这个输出位置和名字，不清楚，还在数据库中，后缀
    # 如果是'分布图模板.mxd23'的话，有点输出后边，比如'mxd23',没有点，全输出
# 各个乡镇的各自缓冲区文件名称
bufName = getvalue_XJQYMC + 'buffer'
outFeatureClass = bufferoutclass + '/' + bufName

# +'/Buffer'+getvalue_XJQYMC+'.shp'
distance = [30,60,90]
bufferunit = 'meters'
# 输出多环缓冲
arcpy.MultipleRingBuffer_analysis(inFeatures,outFeatureClass,distance,bufferunit,'','','OUTSIDE_ONLY')
'''
    
    
    
    #替换缓冲区数据源
    
    
    
    
    
    
    
    # 当选取地图文档是MXD时('CURRENT')，输出的缓冲文件会添加到mxd中
        # 替换环形缓冲区替换掉模板缓冲区的源数据
    # for dellayer in arcpy.mapping.ListLayers(mxd1,'缓冲区',dataframe1):
        # if dellayer.name == u'缓冲区':
        # dellayer.replaceDataSource(bufferoutclass,'SHAPEFILE_WORKSPACE',bufName)
        # print 'updata complete!'
        
        
        # else:
            # 移除缓冲文件图层
            # arcpy.mapping.RemoveLayer(dataframe1,bufName)
            # print bufName
            # print 'del!'
            # if dellayer.name == bufName:
                # arcpy.mapping.RemoveLayer(dataframe1,dellayer)
        

    
    




# print 'ok'

# 日志20190816
    # 老式的cursor，且getValue一直循环获取，速度慢，性能不好

        # cursor = arcpy.SearchCursor(layer)

        # for row in cursor:
            # print row.getValue('CJQYDM')
            # layer.definitionQuery = 'CJQYDM' +'=' +row.getValue('CJQYDM')[:9]



# mxd1.save()
replaceDataSource(workspace_path="C:/test.gdb/Dataset",
                  workspace_type="FILEGDB_WORKSPACE",
                  dataset_name="Dataset/DLTB",
                  validate=True)