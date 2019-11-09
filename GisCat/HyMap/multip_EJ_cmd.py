# -*- coding:cp936 -*-
# 2019 1104
# 廖晨辰

import arcpy, os
from multiprocessing import Process


arcpy.env.overwriteOutput = True
# mxdpath = "" 地图文档的地址
slices_set = [] # 包含多个 地址列表的切片包 的列表（列表的列表）
mxdpaths = []  # 所有地址的列表


def address_clip(mxdpath, process_int):
	"""
	从文件夹中选出mxd文档，将全部mxd地址划分为几个切片然后装进列表中备用
	:param process_int: 运行进程数量
	:param mxdpath:需要出图的mxd文档的路径
	:return: None 但是从内部定义了
	但是从内部声明了两个全局变量列表
		clip_lists = [] # 包含多个 地址列表的切片包 的列表（列表的列表）
		mxdpath_list = [] # 所有地址的列表
	"""
	global slices_set, mxdpaths
	for basename in os.listdir(mxdpath):
		if basename[-3:].lower() == 'mxd':
			realpath = os.path.join(mxdpath, basename)
			# global mxdpath_list
			mxdpaths.append(realpath)
	# mxdpath 收集完毕
	# processInt = 9
	num = len(mxdpaths) // (process_int - 1)  # 20//4 = 5
	for i in xrange(process_int + 1):
		j = i + 1
		aslice = mxdpaths[num * i: num * j]
		print aslice
		# print len(aslice)
		slices_set.append(aslice)
	
	print num
	print len(mxdpaths)
	print type(len(mxdpaths))
# 列表的列表，用来装地址列表切片
# address_clip(ur"G:\test\gst")
# print slices_set

def export_jpeg(path_slice_set, res):
	"""
	获取地址列表切片进行出图处理
	:param path_slice_set: 地址列表 的 一个切片包（列表）
	:param res: 分辨率 int
	:return:
	"""
	count = 1
	for one_path in path_slice_set:
		mxd1 = arcpy.mapping.MapDocument(one_path)
		# print u"正在出图..."
		arcpy.mapping.ExportToJPEG(mxd1, one_path[:-3] + 'jpg', resolution=res)
		del mxd1
		count += 1
		print one_path + " 完成！"


# 可以直接多进程出图
if __name__ == '__main__':
	# 地图文档的地址
	path = raw_input(u"输入文件夹地址： ")
	res = raw_input("输入出图分辨率： ")
	pt = raw_input(" i5推荐4~5进程\ni7推荐7~8进程\n输入进程数：")
	# path = ur"E:\move on move on\公示图"
	# res = 100
	# pt = 8
	path = path
	pt = int(pt)
	print path, res, pt, type(pt)
	address_clip(path, pt)
	print "准备开启多进程通道："
	for path_slice_set in slices_set:
		p = Process(target=export_jpeg, args=(path_slice_set, res))
		p.start()
		print "\t" + "进程通道已打开 " + str(p.pid)
		print "开始出图"

# E:\move on move on\公示图