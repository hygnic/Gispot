# -*- coding:utf8 -*-
# User: hygnic 'liaochen'
# Date: 2019/9/17

"""
文本格式
代码在前：510304107218牛佛镇鞍山村
path1 = ur'G:\MoveOn\df\gst.txt'
图片地址
path2 = ur'G:\MoveOn\df'
GST_rename(path1, path2)
四川命名规范：
GST CJQYDM 08001
"""

import os,re
import tooltk
# print "name:GSTrename"


def gst_rename(txt_path, jpg_path):
	"""
	将两区划定的公示图名称修改成规范的名称
	支持cp936(GBK)和utf8的编码文本的读入
	"""
	txt_file = file(txt_path, "r")
	text_lists = txt_file.readlines()
	jpg_lists = os.listdir(jpg_path)
	for jpg in jpg_lists:
		# 只让图片通过
		if jpg.endswith('jpg'):
			for text in text_lists:
				# txt文本-utf8编码
				try:
					text_field = text[12:].strip().decode('utf8')
					jpg_field = re.findall('\D+', jpg)[1][:-4]
				except UnicodeDecodeError:
					text_field = text[12:].strip().decode('cp936')
				finally:
					
					if text_field == jpg_field:
						oldname = os.path.join(jpg_path, jpg)
						XJQYDM = text[:12]
						newname1 = 'GST'
						newname2 = '08001.jpg'
						GSTname = newname1 + XJQYDM + newname2
						newfile = os.path.join(jpg_path, GSTname)
						showed_msg = jpg_field + " -> " + GSTname
						print showed_msg
						os.rename(oldname, newfile)
						print "Done!"


# 继承u
class App(tooltk.Tooltk):
	# msg_help = "文本格式：代码在前：510304107218牛佛镇鞍山村"
	def __init__(self,master22):
		"""
		:param master22: mian_f , a widget from tool_entrance.py
		"""
		super(App, self).__init__(master22,
								  r"../docs/gstrename.gc",
								  self.confirm_method_g)
		# self.window.grab_set()
		# block1
		self.single_file_block([(u'文本文档', '*.txt'), ('All Files', '*')],
							   u"TXT文本")
		# block2
		self.single_dir_block(u"图片文件夹")
		# 绑定回车键 ，传递的方法必须要传入一个参数（不知道为什么），所以
		# 在下面的confirm_method方法中随便加入了一个无用的形参
		# self.window.bind('<Return>', self.confirm_method)
		

	def confirm_method_g(self):
		"""按下确认button时可以同时获取Entry的值，然后赋值，运行主方法"""
		try:
			# 过去single_file_block和single_dir_block的Entry数据
			self.get_Entry_fromblock(self.input_sfb,self.input_sdb)
			#　开始重命名
			gst_rename(self.block_list[0],
					   self.block_list[1])
			for i in self.block_list:
				print i," type: ",type(i)
			print "---------------"
		except IOError as e:
			errorMsg = e.strerror + "\n" + u"找不到该文件"
			print errorMsg
		finally:
			# 初始化列表
			self.block_list = []
			print "Done"