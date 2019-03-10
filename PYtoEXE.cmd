@echo off
set /p name=
pyinstaller -F %name%.py
del %name%.spec
rmdir __pycache__ /s/q
rmdir build /s/q
if exist %name%.exe del %name%.exe
copy dist\%name%.exe %name%.exe
rmdir dist /s/q