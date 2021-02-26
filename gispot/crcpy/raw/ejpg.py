# -*- coding:cp936 -*-
# lcc

"""
    批量将导出MXD文档导出为JPEG图片
"""
#
# import sys
# sys.path.append("../../GUIs")
# print sys.path
import arcpy,os

# import tooltk


# tooltk.Tooltk().rootwindow.mainloop()
# 设置需要出图mxd文档文件目录
# path = ur"G:\正安县\正安县公示图\400"
# 设置分辨率
# res = 300



arcpy.env.overwriteOutput = True
def export(path, res):
	"""
	批量将导出MXD文档导出为JPEG图片
	:param path: mxd文件夹目录 string
	:param res: 分辨率 int
	:return:
	"""
	for afile in os.listdir(path):
		if afile[-3:].lower() == 'mxd':
			mxd1 = arcpy.mapping.MapDocument(os.path.join(path, afile))
			print u"正在出图..."
			arcpy.mapping.ExportToJPEG(mxd1,
			   os.path.join(path, afile[:-3] + 'jpg'), resolution = res)
			del mxd1
			print 'Done'
		else:
			print u"\n非MXD文件,跳过"
			
if __name__ == '__main__':
	export("path", 300)
	
# app = tooltk.Tooltk()
# app.GUIexport()
#
# app.window.mainloop()

