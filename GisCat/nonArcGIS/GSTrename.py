# -*- coding:utf8 -*-
# User: hygnic 'liaochen'
# Date: 2019/9/17

import os,re,sys
sys.path.append("../GUIs")
import tooltk


def GST_rename(txt_path, jpg_path):
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


# # 代码在前，510304107218牛佛镇鞍山村
# path1 = ur'G:\MoveOn\df\gst.txt'
# # 图片地址
# path2 = ur'G:\MoveOn\df'
# GST_rename(path1, path2)

def poo(s):
	print "a"

# 继承
class App(tooltk.Tooltk):
	def __init__(self):
		super(App, self).__init__()
		self.window.title(u"公示图命名")
		# self.window.grab_set()
		self.single_file_block()
		self.label_1["text"] = u"文本文档"
		self.single_dir_block()
		self.label_2["text"] = u"图片文件夹"
		self.button_confirm["command"] = self.confirm_method
		# 绑定回车键 ，传递的方法必须要传入一个参数（不知道为什么），所以
		# 在下面的confirm_method方法中随便加入了一个无用的形参
		self.window.bind('<Return>', self.confirm_method)
	
	def confirm_method(self):
		self.get_Entry_fromblock()
		print self.block_list
		for i in self.block_list:
			print i
	
	
	# def confirm_method(self):
	# 	"""按下确认button时可以同时获取Entry的值，然后赋值，运行主方法"""
	# 	try:
	# 		self.get_Entry_fromblock()
	# 		# 不知道为什么Entry.grt()获取的 粘贴地址 不是unicode，会出错，
	# 		GST_rename(self.block_list[0],
	# 				   self.block_list[1])
	# 	except IOError as e:
	# 		errorMsg = e.strerror + "\n" + u"找不到该文件"
	# 		print errorMsg
	# 	finally:
	# 		# 初始化列表
	# 		self.block_list = []
	# 		print "Done"
	

if __name__ == '__main__':
	app = App()
	app.window.mainloop()