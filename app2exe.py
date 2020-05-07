
import os

lstIgnore = ['.vscode','.svn','.github','__pycache__','app','doc','pth','wsgi','templates','static','rundata','log','tmp','temp','dist','build']
lstIgnore.extend(['AdminLTE','test'])

def ignorepath(path):
    lst1 = path.split('\\')
    for v1 in lst1:
        if not v1:continue
        if v1 in lstIgnore:return True
    return False

def getRootPath(*args):
    rtn = os.getcwd()
    if args:rtn = os.path.join(rtn, *args)
    rtn = os.path.abspath(rtn)
    return rtn

def save2pth(pathfilename,data):
    try:
        with open(pathfilename,'w', encoding='cp936') as file_:
            file_.write(data)
            file_.close()
    #except :
    except Exception as e:
        print(str(e))
        return False
    return True

if __name__ == "__main__":

    appname = "momo"
    appname_len = len(appname)

    path1 = getRootPath()
    len1 = len(path1)

    lstReturn = []
    lstReturn.append("@echo off")
    lstReturn.append("set a= %1%.py")

    idx = 0
    lst1 = []
    lst1.append("c=%a%")

    for root, dirs, files in os.walk(path1):
        if path1 == root:continue
        root1 = root[len1:]
        if ignorepath(root1):continue
        
        if root1[1:appname_len+1]!= appname:continue
        print("root", root1)  # 当前目录路径
        root1 = root1.lower()

        idx += 1
        #set p0101= -p %cd%\assistant
        lstReturn.append(f"set p{idx}= -p %cd%{root1}")
        lst1.append(f"%p{idx}%")

    #set "c=%a%%pp01%%pp02%%pp03%%pp04%" 
    lstReturn.append("")
    str1 = "".join(lst1)
    str1 = f'set "{str1}"'
    lstReturn.append(str1)

    lstReturn.append("")
    lstReturn.append("set fd=-D")

    lstReturn.append("")
    lstReturn.append('if "%2%"=="f" (')
    lstReturn.append('    set "fd=-F"')
    lstReturn.append(')')

    lstReturn.append("")
    lstReturn.append('if "%2%"=="F" (')
    lstReturn.append('    set "fd=-F"')
    lstReturn.append(')')
    
    lstReturn.append("")
    lstReturn.append('rem echo %1%')
    lstReturn.append('rem echo  %c%')

    lstReturn.append("")
    lstReturn.append('python -O -m PyInstaller -y %fd% %c%')
    
    str1 = '\r\n'.join(lstReturn)

    if os.path.exists(appname):
        pth = r"%s\py2exe.bat" % appname
        save2pth(pth,str1)
    else:
        print("App Name is not Exists",appname)


