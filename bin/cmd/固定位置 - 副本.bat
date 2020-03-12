@echo off
set rr="HKCU\Console\%%SystemRoot%%_system32_cmd.exe"
reg add %rr% /v "WindowPosition" /t REG_DWORD /d 0x010e0140 /f>nul
::WindowPosition表示窗口位置，高四位为上，低四位为左，距屏幕上沿10eH=270，距屏幕左沿140H=320。
reg add %rr% /v "ScreenBufferSize" /t REG_DWORD /d 0x000a002d /f>nul
::ScreenBufferSize表示缓冲区尺寸，高四位为高度，低四位为宽度，高aH=10行，宽2dH=45列。
reg add %rr% /v "WindowSize" /t REG_DWORD /d 0x000a002d /f>nul
::WindowSize表示窗口尺寸，高四位为高度，低四位为宽度，高aH=10行，宽2dH=45列。
::也可以用mode con cols=45 lines=10来设置窗口尺寸，cols设置宽度，lines设置高度。
if not defined ff (set ff=0&start cmd /c %0&exit)
COLOR 8B
::color设置背景色和字体颜色
pause