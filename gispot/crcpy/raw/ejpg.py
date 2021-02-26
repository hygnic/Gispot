# -*- coding:cp936 -*-
# lcc

"""
    ����������MXD�ĵ�����ΪJPEGͼƬ
"""
#
# import sys
# sys.path.append("../../GUIs")
# print sys.path
import arcpy,os

# import tooltk


# tooltk.Tooltk().rootwindow.mainloop()
# ������Ҫ��ͼmxd�ĵ��ļ�Ŀ¼
# path = ur"G:\������\�����ع�ʾͼ\400"
# ���÷ֱ���
# res = 300



arcpy.env.overwriteOutput = True
def export(path, res):
	"""
	����������MXD�ĵ�����ΪJPEGͼƬ
	:param path: mxd�ļ���Ŀ¼ string
	:param res: �ֱ��� int
	:return:
	"""
	for afile in os.listdir(path):
		if afile[-3:].lower() == 'mxd':
			mxd1 = arcpy.mapping.MapDocument(os.path.join(path, afile))
			print u"���ڳ�ͼ..."
			arcpy.mapping.ExportToJPEG(mxd1,
			   os.path.join(path, afile[:-3] + 'jpg'), resolution = res)
			del mxd1
			print 'Done'
		else:
			print u"\n��MXD�ļ�,����"
			
if __name__ == '__main__':
	export("path", 300)
	
# app = tooltk.Tooltk()
# app.GUIexport()
#
# app.window.mainloop()

