#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2021/2/20 20:16
# Reference:
"""
Description: 使用上下文管理器实现xlwings对excel文件的关闭和开启
Usage:
"""
# ---------------------------------------------------------------------------
from contextlib import contextmanager
try:
    import xlwings as xw
except ImportError as e:
    print "No module named xlwings"


"""--------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------"""
# old method
# try:
#     app1 = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
#     app1.display_alerts = False  # 关闭Excel的提示和警告信息
#     app1.screen_updating = False
#     wb1 = app1.books.open(sheet_p)
#     wbs1 = wb1.sheets["sheet1"]
#
#     wbs1.range("a1:a1").value = 3
#
#     print app1.books
#     print app1.pid
#
#
#     wb1.save()
#
# finally:
#     app1.quit()

"""--------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------"""

@contextmanager
def open_xlwings(input_file, output=None):
    app = xw.App(visible=False, add_book=False)  # 只打开不新增工作簿
    app.display_alerts = False  # 关闭Excel的提示和警告信息
    app.screen_updating = False
    print "input_file:",input_file
    wb = app.books.open(input_file)
    print "File Name: {}".format(app.books)
    print "Pid: {}".format(app.pid)
    sheet = wb.sheets[0]  # sheet = wb.sheets["sheet1"]
    # sheet.range("a1").value = [1,2,3,4,5,6]
    
    # 行数计算
    # rows_count = sheet.api.UsedRange.Rows.count
	# year = sheet.range("A1:A"+str(rows_count)).value
    
    try:
        yield sheet # 返回 sheet
    except Exception as e:
        info = "with an error {}".format(e)
        raise
    else:
        if output:
            wb.save(output)
        else:
            wb.save()
    finally:
        print "Quit Xlwings"
        app.quit()

# test
if __name__ == '__main__':
    # sheet_p = r"G:\test.xlsx"
    sheet_p = r"G:\test\test.xlsx"
    with open_xlwings(sheet_p, ) as open_xw:
    # with open_xlwings(sheet_p, r"G:\test\te22st.xlsx") as open_xw:
        open_xw.range("a1").value = [222,4555]
        print open_xw
        