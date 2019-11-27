# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/10
import os,sys

real = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(real,"bin"))
apppath = r"bin\tool_entrance.py"

import tool_entrance

if __name__ == '__main__':
	entrance = tool_entrance.AppEntrance()
	entrance.menu()
	entrance.rootwindow.mainloop()