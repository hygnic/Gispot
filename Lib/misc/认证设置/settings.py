# -*- coding: utf8 -*-
# User: hygnic 廖晨辰
# Date: 2019/10/2
import datetime,os
import arcpy
import sys
import hashlib
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
				arcpy.AddMessage("		Done!")
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
				return  False
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


# create_authentication_setting("2020-3-3")

def change_authentication_time():
	archygnic_path = os.path.dirname(sys.executable) + "/archygnic"
	archygnic_arctime = archygnic_path + "/arctime"
	if not os.path.isdir(archygnic_path):
		os.makedirs(archygnic_path)
	with open(archygnic_arctime,"w") as setting_file:
		now_time = datetime.datetime.now()
		add_time = datetime.timedelta(days=90)
		auth_time = now_time + add_time
		str_time = auth_time.strftime("%Y-%impure_data-%d")
		setting_file.write(str_time)



def md5(pw):
	"""
	md5加密
	:param pw密码
	:return:
	"""
	# pw_str = str(pw)
	# 使用md5算法， 加盐 cnpt,jiayan
	obj = hashlib.md5(pw.encode("utf8"))
	# 编码为字节
	# obj.update(pw.encode("utf8"))
	return obj.hexdigest()

try:
	print md5("1q23lyc45j")
	arcpy.AddMessage(md5("1q23lyc45j"))
except:
	print "--error！--"
else:
	pass

if __name__ == "__main__":
	print "ok"
	# 获取密码
	password = arcpy.GetParameterAsText(0)
	# password = "1q23lyc45j"
	arcpy.AddMessage(password)
	arcpy.AddMessage(type(password))
	arcpy.AddMessage(md5(password))
	print md5(password)
	if md5(password) == "cd36b12d855392eab8158c0488c86307":
		change_authentication_time()
		arcpy.AddMessage("	Done!!")
	# except Exception as e:
	# 	arcpy.AddMessage(e)
	else:
		arcpy.AddMessage("failure") 