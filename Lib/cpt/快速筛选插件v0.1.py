# -*- coding: cp936 -*-
import arcpy,os,re
path1 = ur'G:\正安县\正安县公示图\成果'
for names in os.listdir(path1):
    if names.endswith('.mxd'):
        #a = re.findall('\D+',names)[1]
        a = names
        a = a[:-4]
        
        # name = names[7:-4]
        # print 'ff '+'= '+ "'" + a + "' OR "
        print a
        print len(os.listdir(path1))
        
