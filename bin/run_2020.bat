@echo off
set rr="HKCU\Console\%%SystemRoot%%_system32_cmd.exe"
reg add %rr% /v "WindowPosition" /t REG_DWORD /d 0x00d70548 /f>nul
::WindowPosition表示窗口位置，高四位为上，低四位为左，距屏幕上沿00d7H=215，距屏幕左沿54dH=1357。548H=1352
::reg add %rr% /v "ScreenBufferSize" /t REG_DWORD /d 0x000a002d /f>nul
::ScreenBufferSize表示缓冲区尺寸，高四位为高度，低四位为宽度，高000aH=10行，宽002dH=45列。
::reg add %rr% /v "WindowSize" /t REG_DWORD /d 0x0028002d /f>nul
::WindowSize表示窗口尺寸，高四位为高度，低四位为宽度，高002aH=42行，宽0028H=40列  002dH = 45
mode con cols=45 lines=40
if not defined ff (set ff=0&start cmd /c %0&exit)
::pause
python2 Gispot.py