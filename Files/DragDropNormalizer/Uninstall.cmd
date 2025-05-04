@echo off
title DragDropNormalizer Uninstaller

echo Please, make sure you are running this file as administrator
echo Uninstalling DragDropNormalizer...

reg delete HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v "DragDropNormalizer" /f
del %WINDIR%\DragDropNormalizer.exe

echo DragDropNormalizer has been sucessfully uninstalled

:end
pause