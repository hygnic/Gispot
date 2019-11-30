# -*- coding:utf8 -*-
# User: hygnic 'liaochen'
# Date: 2019/9/17

"""
公示图名称转换
510304107218，改为国家标准（行政区划代码12位加位顺序码）

"""

import os,re
import tooltk
# print "name:GSTrename"


def gst_trans(jpg_path):
	"""
	510304107218，改为国家标准（行政区划代码12位加位顺序码）
	:param jpg_path: 图片文件夹
	:return:
	"""
	jpg_lists = os.listdir(jpg_path)
	for jpg in jpg_lists:
		# 只让图片通过
		if jpg[-3:].lower() == 'jpg':
			if jpg[:3].lower() == "gst":
				oldname = os.path.join(jpg_path, jpg)
				new_jpg = jpg[:15]
				newname1 = '001.jpg'
				GSTname = new_jpg + newname1
				newfile = os.path.join(jpg_path, GSTname)
				showed_msg = new_jpg + " -> " + GSTname
				print showed_msg
				os.rename(oldname, newfile)
				print "Done!"

# gst_trans(ur"F:\正安县\gshitu")

# 继承
class App(tooltk.Tooltk):
	# msg_help = "文本格式：代码在前：510304107218牛佛镇鞍山村"
	def __init__(self):
		super(App, self).__init__(u"公示图名称")
		self.button_confirm["command"] = self.confirm_method
		# self.window.grab_set()
		# block1
		self.single_dir_block(u"图片文件夹")
		self.read_help(r"docs\trans_gst")

	def confirm_method(self):
		"""按下确认button时可以同时获取Entry的值，然后赋值，运行主方法"""
		try:
			# 过去single_file_block和single_dir_block的Entry数据
			self.get_Entry_fromblock(self.input_sdb)
			#　开始重命名
			gst_trans(self.block_list[0])
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


if __name__ == '__main__':
	app = App()
	app.window.mainloop()