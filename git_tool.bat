@echo off

set code=D:\code
set knowledge=D:\knowledge
set operation=D:\operation_system
set message="none"

set /p input=Update all data? (y/n) 
if "%input%"=="y" goto all
if "%input%"=="n" goto common

:all
call :x e "operation pull"
cd /d %operation% && git pull
call :x a "done"
echo=
echo=
echo=
call :x e "operation push"
cd /d %operation% && git pull && git add -A && git commit -m %message% && git push
call :x a "done"
echo=
echo=
echo=


:common
call :x e "knowledge pull"
cd /d %knowledge% && git pull
call :x a "done"
echo=
echo=
echo=
call :x e "knowledge push"
cd /d %knowledge% && git pull && git add -A && git commit -m %message% && git push
call :x a "done"
echo=
echo=
echo=

call :x e "code pull"
cd /d %code% && git pull
call :x a "done"
echo=
echo=
echo=
call :x e "code push"
cd /d %code% && git pull && git add -A && git commit -m %message% && git push
call :x a "done"
echo=
echo=
echo=

pause

goto :eof
:x
echo. >%2&findstr /a:%1 . %2*&del %2

