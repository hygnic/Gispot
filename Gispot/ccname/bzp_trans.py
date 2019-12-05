# -*- coding: utf-8 -*-
# User: hygnic liaochen
# Date: 2019/9/17

"""
标志牌照片改为国家标准（行政区划代码12位+顺序码4位）
"""
import os, re
import tooltk

def bzp_trans(jpg_path):
	jpg_list = os.listdir(jpg_path)
	for jpg in jpg_list:
		if jpg.endswith('jpg'):
			oldname = os.path.join(jpg_path,jpg)
			preff = jpg[:12]
			suff = '09001.jpg'
			newname = preff+suff
			newfile = os.path.join(jpg_path, newname)
			showed_msg = jpg + " -> " + newname
			print showed_msg
			os.rename(oldname, newfile)
			print 'ok'



# 继承
class App(tooltk.Tooltk):
	# msg_help = "文本格式：代码在前：510304107218牛佛镇鞍山村"
	def __init__(self):
		super(App, self).__init__(u"分布图名称")
		self.button_confirm["command"] = self.confirm_method
		# self.window.grab_set()
		# block1
		self.single_dir_block(u"图片文件夹")
		self.read_help(r"docs\gstrename")
	
	def confirm_method(self):
		"""按下确认button时可以同时获取Entry的值，然后赋值，运行主方法"""
		try:
			# 过去single_file_block和single_dir_block的Entry数据
			self.get_Entry_fromblock(self.input_sfb, self.input_sdb)
			# 　开始重命名
			fbt_trans(self.block_list[0])
			for i in self.block_list:
				print i, " type: ", type(i)
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