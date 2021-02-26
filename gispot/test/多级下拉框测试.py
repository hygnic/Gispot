# -*- coding:utf-8 -*-
# User: liaochenchen
# Date: 2019/12/10
# python2.7

# import Tkinter as tk
# import ttk
#
# wuya = tk.Tk()
# wuya.remove_sth("wuya")
# wuya.geometry("300x200+10+20")
#
# # 创建下拉菜单
# cmb = ttk.Combobox(wuya)
# cmb['value'] = ('上海','北京','天津','广州')
# cmb.pack()
#
# cmb1 = ttk.Combobox(cmb)
# cmb1.pack()
#
# wuya.mainloop()

import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        menubutton = tk.Menubutton(self, text="Choose wisely",
                                   indicatoron=True, borderwidth=1, relief="raised")
        menu = tk.Menu(menubutton, tearoff=False)
        menubutton.configure(menu=menu)
        menubutton.pack(padx=10, pady=10)
        
        self.choices = {}
        for choice in ("Iron Man", "Superman", "Batman"):
            self.choices[choice] = tk.IntVar(value=0)
            menu.add_checkbutton(label=choice, variable=self.choices[choice],
                                 onvalue=1, offvalue=0,
                                 command=self.printValues)
    def printValues(self):
        for name, var in self.choices.items():
            print "%s: %s" % (name, var.get())

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

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
