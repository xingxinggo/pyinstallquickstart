
@echo off
    set a= %1%.spec 
   
python -O -m PyInstaller -y %a% 
