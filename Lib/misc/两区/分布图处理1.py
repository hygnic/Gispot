# -*- coding: cp936 -*-
# 2019 08 15 廖晨辰


import arcpy
import datetime
import os

time1 = datetime.datetime.now()
time2 = datetime.datetime.strptime("2020-1-1", "%Y-%impure_data-%d")
if time1 > time2:
	arcpy.AddError(u'\n\n工具损坏！！联系廖晨辰\n\n')
else:
	# 模板目录，只需要一个设置好了的mxd文件
	# template = 'G:/都江堰/都江堰分布图0815/编程试验文件/中兴镇.mxd'
	template = 'CURRENT'
	# template = template.decode('utf-8')
	
	
	# 设置输出目录
	outputclass = arcpy.GetParameterAsText(0)
	# outputclass = u'G:/南江县/南江分布图/输出地图文档'
	# outputclass = outputclass.decode('utf-8')
	# outputclass = outputclass.decode('gb2312')
	
	# 设置缓冲区文件存放目录
	bufferoutclass = arcpy.GetParameterAsText(1)
	# bufferoutclass = u'G:/南江县/南江分布图/缓冲区文件'
	# bufferoutclass = bufferoutclass.decode('gb2312')
	
	# 可以进行覆盖
	arcpy.env.overwriteOutput = True
	
	# 读取文件
	mxd1 = arcpy.mapping.MapDocument(template)
	print mxd1.title
	dataframe1 = arcpy.mapping.ListDataFrames(mxd1)[0]
	dataframe2 = arcpy.mapping.ListDataFrames(mxd1)[1]
	
	# 必须将第一个图层设置为激活图层，否则退出程序
	if not mxd1.activeDataFrame == dataframe1:
		arcpy.AddError(u'\n\n请激活第一个数据框！！！！\n\n')
	else:
		# 创建数据库容纳XJQY的各个单独的区域，为缓冲区的建立做准备
		tempDB = u'中间处理暂存数据库.gdb'
		arcpy.CreateFileGDB_management(bufferoutclass, tempDB)
		
		print dataframe1.name + u'图框读取成功'
		print dataframe2.name + u'图框读取成功'
		
		# 匹配字段是CJQYDM
		layerlist1 = ['标志牌', '村名']
		
		# 匹配字段是XJQYDM
		layerlist2 = ['XJQY', '乡镇驻地', '村委会', 'DZDW', 'XZDW', '村界']
		
		# 从该图层中读取属性表信息，将它传递与其他图层
		datalayer = arcpy.mapping.ListLayers(mxd1, 'XJQY', dataframe1)[0]
		datalayer.definitionQuery = ""
		cursor = arcpy.da.SearchCursor(datalayer, ('XJQYDM', 'XJQYMC', 'XJXZQ'))
		namelist = []
		arcpy.AddMessage('定义语句查询...')
		# 读取XJQYDM
		for row in cursor:
			getvalue_XJQYDM = row[0]
			getvalue_XJQYMC = row[1]
			getvalue_MC = row[2]
			# 定义查询
			# '标志牌','村名'
			for onelayerlist in layerlist1:
				layer = arcpy.mapping.ListLayers(mxd1, onelayerlist, dataframe1)[0]
				# 有时候标志牌暂时没有
				if not layer.isBroken:
					layer.definitionQuery = '"' + 'CJQYDM' + '"' + ' like' \
											+ " '" + getvalue_XJQYDM[:9] + "%'"
				
				# 'XJQY','乡镇驻地','村委会','DZDW','XZDW','村界'
			for onelayerlist in layerlist2:
				layer = arcpy.mapping.ListLayers(mxd1, onelayerlist, dataframe1)[0]
				# layer.definitionQuery = ''
				layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
				
				# 两区片块及作物类型
			layer = arcpy.mapping.ListLayers(mxd1, '两区片块及作物类型', dataframe1)[0]
			layer.definitionQuery = '"' + 'LQPKDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM + "%'"
			
			# LQDK融合
			layer = arcpy.mapping.ListLayers(mxd1, 'LQDK融合', dataframe1)[0]
			layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
			
			# DLTB融合_路河_方便出图
			layer = arcpy.mapping.ListLayers(mxd1, 'DLTB融合_路河_方便出图', dataframe1)[0]
			layer.definitionQuery = '"' + 'QSDWDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM + "%'"
			
			# DLTB融合
			layer = arcpy.mapping.ListLayers(mxd1, 'DLTB融合', dataframe1)[0]
			layer.definitionQuery = '"' + 'QSDWDM' + '"' + ' LIKE ' + "'" + getvalue_XJQYDM + "%'"
			
			# 修改第二个图框的定义查询
			layer = arcpy.mapping.ListLayers(mxd1, 'XJQY', dataframe2)[0]
			layer.definitionQuery = '"' + 'XJQYDM' + '"' + ' = ' + "'" + getvalue_XJQYDM + "'"
			
			# 设置地图文档中的文字元素
			for elm in arcpy.mapping.ListLayoutElements(mxd1, 'TEXT_ELEMENT'):
				if elm.name == 'BT1':
					elm.text = u'%s%s"两区"农田空间分布图' % (getvalue_MC, getvalue_XJQYMC)
				if elm.name == 'BT2':
					elm.text = u'%s在%s的位置示意图' % (getvalue_XJQYMC, getvalue_MC)
			
			# 缩放调整尺寸
			layer = arcpy.mapping.ListLayers(mxd1, 'XJQY', dataframe1)[0]
			dataframe1.extent = layer.getSelectedExtent()
			dataframe1.scale = 10000
			
			arcpy.env.workspace = bufferoutclass
			# 将选择的数据导入进数据库中
			arcpy.FeatureClassToGeodatabase_conversion(datalayer,
													   bufferoutclass + '/' + tempDB)
			# 将数据库中文件重命名
			prename = bufferoutclass + '/' + tempDB + '/' + 'GPL0'
			# prename = bufferoutclass + '/' + tempDB + '/' + 'XJQY'
			
			# arcpy.AddMessage(os.listdir(bufferoutclass + '/' + tempDB))
			
			arcpy.Rename_management(prename, getvalue_XJQYMC)
			
			namelist.append(getvalue_XJQYMC)
			# 另存地图文档
			mxd1.saveACopy(outputclass + '/' + getvalue_XJQYMC + '.mxd')
		del cursor
		
		# 排序列表
		namelist.sort()
		
		arcpy.env.workspace = bufferoutclass
		arcpy.AddMessage('设置缓冲区...')
		
		for aname in namelist:
			# 生成缓冲区
			inFeatures = tempDB + '/' + aname
			outFeatureClass = bufferoutclass + '/' + aname
			distance = [30, 60, 90]
			bufferunit = 'meters'
			arcpy.MultipleRingBuffer_analysis(inFeatures, outFeatureClass, distance,
											  bufferunit, '', '', 'OUTSIDE_ONLY')
			
			dellayer = arcpy.mapping.ListLayers(mxd1, '', dataframe1)[0]
			if not dellayer.name == 'XJQY':
				arcpy.mapping.RemoveLayer(dataframe1, dellayer)
			print 'buffer complete!'
		
		# 让刚刚生成的环形缓冲区文件替换个乡镇mxd中的'缓冲区'图层
		# 读取生成的地图文档
		
		# import arcpy,os
		# outputclass = u'G:\\南江县\\南江分布图\\输出地图文档'
		# bufferoutclass = u'G:\\南江县\\南江分布图\\缓冲区文件'
		# tempDB = u'中间处理暂存数据库.gdb'
		for newfile in os.listdir(outputclass):
			if newfile[-3:].lower() == 'mxd':
				# 将名字选出来
				xxxx = newfile[:-4]
				# 避免我们将区县级别的mxd加入mxd目录，由于找不到相应缓冲区而报错
				if xxxx in namelist:
					newMXD = arcpy.mapping.MapDocument(os.path.join(outputclass, newfile))
					# versionpath = outputclass+'/'+version
					newlayer = arcpy.mapping.ListLayers(newMXD, '缓冲区')[0]
					# 将与mxd文档名字相同的缓冲区替换进去
					newlayer.replaceDataSource(bufferoutclass, 'SHAPEFILE_WORKSPACE', xxxx)
					newMXD.save()
		
		arcpy.Delete_management(bufferoutclass + '/' + tempDB)
		arcpy.AddMessage('Done!')
