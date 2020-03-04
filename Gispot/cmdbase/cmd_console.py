# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2020/3/4

import os
from multiprocessing import Process

class Starter1(object):
	def __init__(self):
		self.beg()
		
	@staticmethod
	def beg():
		base_dir = os.path.abspath(__file__)
		upper_dir = os.path.dirname(base_dir)
		target_dir = os.path.join(upper_dir, "export_bash.py")
		target_dir = os.path.abspath(target_dir)
		print os.path.isfile(target_dir)
		print target_dir
		comd = "python " + target_dir
		os.system(comd)
	
def xx():
	with open(r"G:\test\4554","w") as f:
		f.write("hh")
		f.close()
		
if __name__ == '__main__':
	p = Process(target=Starter1)
	# ff = Starter1()
	p.start()