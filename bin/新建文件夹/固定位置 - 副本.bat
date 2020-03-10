@echo off

mode con cols=85 lines=25
if not defined ff (set ff=0&start cmd /c %0&exit)
COLOR 8B
::color设置背景色和字体颜色
pause