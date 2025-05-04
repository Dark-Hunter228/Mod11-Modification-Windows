@echo off
title DragDropNormalizer Installer

echo Please, make sure you are running this file as administrator
echo Installing DragDropNormalizer...

cd %~dp0%
copy DragDropNormalizer.exe %WINDIR%\DragDropNormalizer.exe
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v "DragDropNormalizer" /d %WINDIR%\DragDropNormalizer.exe

cd %WINDIR%
start DragDropNormalizer.exe

echo DragDropNormalizer has been sucessfully installed
pause