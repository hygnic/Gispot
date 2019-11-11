# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/11/11
import os



# for basename in paths_list:
# 	if basename[-3:].lower() == 'mxd':
# 		# print basename.decode("cp936")
# 		realpath = os.path.join(mxdpath, basename)
		# print realpath
# print len(paths_list)
newlist = []
def chunks_list(mxdpath,process_core):
	
	paths_list = os.listdir(mxdpath)
	print "all path: ", len(paths_list)
	aslise = len(paths_list) // process_core
	print "path_list_num: ",aslise
	global newlist
	def chunks(l, n):
		# Yield successive n-sized chunks from l.
		for i in xrange(0, len(l), n):
			path_slice = l[i:i + n]
			newlist.append(path_slice)
		return newlist
	
	f= chunks(paths_list, aslise)
	print "f's list: ",len(f)
	print f


mxdpath = r"G:\test\gst"
process_core = 3
chunks_list(mxdpath,process_core)