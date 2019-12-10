# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/10
# python2.7

import Tkinter as tk
import ttk

wuya = tk.Tk()
wuya.title("wuya")
wuya.geometry("300x200+10+20")

# 创建下拉菜单
cmb = ttk.Combobox(wuya)
cmb['value'] = ('上海','北京','天津','广州')
cmb.pack()

cmb1 = ttk.Combobox(cmb)
cmb1.pack()

wuya.mainloop()

def menu():
	# User: hygnic
	# Date: 2018/8/27
	
	menu = {
		'China': {
			'sichuan': {
				'chengdu': {}
			},
			'xingjiang': {
				'wulumuqi': {}
			},
			'beijing': {
				'haidian': {}
			},
		},
		'America': {
			'ohio': {
				'columbus': {}
			},
			'colorado': {
				'denver': {}
			},
			'florida': {
				'tallahassee': {}
			},
		},
		'Italy': {
			'don\'t know': {
				'don\'t know': {}
			},
			'don\'t know': {
				'don\'t know': {}
			},
			'don\'t know': {
				'don\'t know': {}
			}
		}
	}
	
	current_layer = menu
	parent_layer = []
	
	while True:
		for key in current_layer:
			print(key)
		choice = input("enter your choice").strip()
		if len(choice) == 0:
			continue
		if choice in current_layer:
			parent_layer.append(current_layer)
			# 再次进入循环
			current_layer = current_layer[choice]
		elif choice == 'b':
			if parent_layer:
				current_layer = parent_layer.pop()
			else:
				print('无此项')
		else:
			print('无此项')
