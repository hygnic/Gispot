@echo off &color a&setlocal enabledelayedexpansion&title %~n0
mode con lines=18 cols=40
for /f "skip=1 tokens=1-2 delims= " %%i in ('wmic desktopmonitor get screenwidth^,screenheight') do (
for /l %%b in (1 1 4) do (echo.)
echo by 李进
for /l %%b in (1 1 3) do (echo.)
for /l %%a in (1 1 40) do (set /p =*<nul)
echo * 屏高： %%i *
echo * *
echo * 屏宽： %%j *
for /l %%a in (1 1 40) do (set /p =*<nul)
for /l %%b in (1 1 4) do (echo.)
)
pause