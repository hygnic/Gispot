# -*- coding: utf-8 -*-
# User: liaochenchen, hygnic
# Date: 2019/11/30

import sys

sys.path.append("../../libs")
from hyconf import _gPath

ac  = _gPath.Path_GC()
s =ac.explode_mulitp
print s

# path = "../../libs/_gPath.py"

# with open(path,"r") as f:
# 	s = f.readlines()
# 	for i in s:
# 		print i