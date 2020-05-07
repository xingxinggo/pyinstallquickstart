@echo off

set a= %1%.py

set p1= -p %cd%\momo





set "c=%a%%p1%"



set fd=-D



if "%2%"=="f" (

    set "fd=-F"

)



if "%2%"=="F" (

    set "fd=-F"

)



rem echo %1%

rem echo  %c%



python -O -m PyInstaller -y %fd% %c%
