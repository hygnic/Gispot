# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/10/12
import datetime,os
import arcpy,sys
# import tovsr

def create_authentication_setting(time):
	"""
	time, flag = False
	"""
	# 检查存在并创建文件夹
	# sys.executable D:\Program Files\ArcGIS\Desktop10.4\bin\ArcMap.exe
	# 全局申明
	# global archygnic_arctime,archygnic_path
	archygnic_path = os.path.dirname(sys.executable) + "/archygnic"
	archygnic_arctime = archygnic_path + "/arctime"

	if not os.path.isdir(archygnic_path):
		# os.makedirs(archygnic_path)
		os.mkdir(archygnic_path)

	# 检查 文本存在
	if os.path.isfile(archygnic_arctime):
		# 文本是否有内容
		# 8 字节
		if os.path.getsize(archygnic_arctime) != 0:
			with open(archygnic_arctime, "r") as atime_file:
				atime = atime_file.readline()
			now_time = datetime.datetime.now()
			authentication_time = datetime.datetime.strptime(atime,
															 "%Y-%impure_data-%d")
			if now_time < authentication_time:
				# 认证成功
				arcpy.AddMessage("\t\nauthentication\n")
				return True
			else:
				return False
		# 無内容
		else:
			with open(archygnic_arctime, "w") as atime_file:
				atime_file.write(time)
			now_time = datetime.datetime.now()
			authentication_time = datetime.datetime.strptime(time,
															 "%Y-%impure_data-%d")
			if now_time < authentication_time:
				# 认证成功
				return True
			else:
				return False
	# 无文本
	else:
		# 创建文本
		# open(archygnic_arctime, "w+").close()
		with open(archygnic_arctime, "w") as atime_file:
			arcpy.AddMessage("ok")
			atime_file.write(time)
		now_time = datetime.datetime.now()
		authentication_time = datetime.datetime.strptime(time,
														 "%Y-%impure_data-%d")
		if now_time < authentication_time:
			return True
		else:
			return False


create_authentication_setting("2017-7-7")
# tovsr.message()